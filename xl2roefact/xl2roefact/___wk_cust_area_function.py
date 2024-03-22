#
# work area to clean and generalize a function to solve CUSTOMER INFO:
# -1. to replace as separated function the existing code for customer info
# -2. to generalize it to work for customer info, but a "CUSTOMER" op/cmd to be sent as parameter
# -3. to be able to work for op/cmd "SUPPLIER"
# -4. to be placed in `rdinv.py` module and to do work in new environment without disturbing it for existing functionalities
#     ... ie, to not induce lateral effects
# 5. location in rdinv.py where to call this function marked `#FIXME.UNIF.PARTNER.DATA`

#... ... ... #NOTE imports section NOT NEEDED. It is for testing to avoid error due to its missing
from . import config_settings
from rdinv import get_excel_data_at_label
from rdinv import PATTERN_FOR_PARTNER_ID
from rdinv import PATTERN_FOR_INVOICE_CUSTOMER_SUBTABLE_MARKER
from rdinv import PATTERN_FOR_CUSTOMER_LEGAL_NAME
#... ... ... #NOTE imports section NOT NEEDED. It is for testing to avoid error due to its mi




# TODO: constants area code:
#    - must stay in `rdinv.py` in constants area
#    - checked & define in `config_settings.py` & `data/app_settings.yml`
#    - most cases they should be like their ...CUSTOMER... equivalent
PATTERN_FOR_INVOICE_SUPPLIER_SUBTABLE_MARKER = config_settings.PATTERN_FOR_INVOICE_SUPPLIER_SUBTABLE_MARKER
PATTERN_FOR_SUPPLIER_LEGAL_NAME = config_settings.PATTERN_FOR_SUPPLIER_LEGAL_NAME
DEFAULT_SUPPLIER_COUNTRY = config_settings.DEFAULT_SUPPLIER_COUNTRY  #FIXME thia should be set as` global` & could exists. Check it...





# TODO: new function to be moved in `rdinv.py`
# TODO: to call in rdinv.py @ marker `FIXME.UNIF.PARTNER.DATA` (in CHANGELOG there are more details)
def get_partner_data(
    partner_type: str,  # IN
    *,
    param_invoice_header_area: dict,  # INOUT
    # ...more params here
) -> dict:
    """Get invoice partener data from Excel.

    NOTE: function induce necessary side effects and works only if located in `rdinv.py`

    Args:
        `partner_type`: one of "CUSTOMER", "SUPPLIER" or "OWNER" to specify for what kind of parner get data. The value "OWNER" is designed to get data from an outside database / file (master data).
        `param_invoice_header_area`: outside `param_invoice_header_area` as used and needed in `rdinv()`. This function will write back in this variable.

    Return:
        `dict`: with parner data. Dictionary is in form needed in `rdinv()` function.
    """

    # normalize partner_type for easier usage and more flexibility to developers misusing
    partner_type = partner_type.upper().strip()
    # unify search patterns and other constants function of partner_type
    if partner_type == "CUSTOMER":
        UNIF_PATTERN_FOR_INVOICE_PARTNER_SUBTABLE_MARKER = PATTERN_FOR_INVOICE_CUSTOMER_SUBTABLE_MARKER
        UNIF_PATTERN_FOR_PARTNER_LEGAL_NAME = PATTERN_FOR_CUSTOMER_LEGAL_NAME
        UNIF_DEFAULT_PARTNER_COUNTRY = DEFAULT_CUSTOMER_COUNTRY
        unif_partner_area_key = "customer_area"
        ...  #FIXME: more refactoring code here?
    elif partner_type =="SUPPLIER":
        # NOTE: pls be patient. Here will raise errs because used EXPECTED constant names. Check `config_settings.py` and adjust accordingly
        UNIF_PATTERN_FOR_INVOICE_PARTNER_SUBTABLE_MARKER = PATTERN_FOR_INVOICE_SUPPLIER_SUBTABLE_MARKER
        UNIF_PATTERN_FOR_PARTNER_LEGAL_NAME = PATTERN_FOR_SUPPLIER_LEGAL_NAME
        UNIF_DEFAULT_PARTNER_COUNTRY = DEFAULT_SUPPLIER_COUNTRY
        unif_partner_area_key = "supplier_area"
        ...  #FIXME: more refactoring code here?
    elif partner_type == "OWNER":  # subject to load SUPPLIER data from external data source
        ...  #FIXME: more refactoring code here?
    else:
        # accept only known operations
        raise Exception("partner_type parameter not recognized value")
    #
    # find invoice customer ==> "cac:AccountingCustomerParty
    invoice_partner_info = get_excel_data_at_label(
        pattern_to_search_for=UNIF_PATTERN_FOR_INVOICE_PARTNER_SUBTABLE_MARKER,  #FIXME constant adjusted in refactoring process
        worksheet=ws,
        area_to_scan=(param_invoice_header_area["start_cell"], param_invoice_header_area["end_cell"]),
        targeted_type=str
    )  # returned info: `{"value": ..., "location": (row..., col...)}`
    # set a dedicated area to search for customer
    _area_to_search_start_cell = [  # use `label_location` as being supposed "most far away" from effective-good info, so more chances to find info
        0 if invoice_partner_info["label_location"][0] <= 0 else invoice_partner_info["label_location"][0] - 1,  # set one line up if this line exists
        invoice_partner_info["label_location"][1],
    ]
    if ws.index(*_area_to_search_start_cell).strip() == "":  # prev set was for one line up but if that cell is blank remake it (ie, do a +1)
        _area_to_search_start_cell[0] += 1
    # from `_area_to_search_start_cell` go down up a blank (empty cell)
    _last_ok_position = list([0, 0])
    for __i in range(_area_to_search_start_cell[0], ws.size[0] + 1):  # scan rest of lines for a blank one
        _crt_scanned_cell_idx = (__i, _area_to_search_start_cell[1])
        _crt_scanned_cell_val = ws.index(*_crt_scanned_cell_idx)
        if _crt_scanned_cell_val.strip() == "":
            break  # case where stop
        _last_ok_position = copy.deepcopy(_crt_scanned_cell_idx)  # save current position to be used after a break in other iteration
    _area_to_search_end_cell = [
        _last_ok_position[0],
        ws.size[1] if _last_ok_position[1] > ws.size[1] else _last_ok_position[1] + 1,  # set one row right if this row exists
    ]
    # persist `_area_to_search` for next steps & save its key-info in associated invoice JSON (for further references)
    _area_to_search = (tuple(_area_to_search_start_cell), tuple(_area_to_search_end_cell))
    param_invoice_header_area[unif_partner_area_key] = {
        "area_info": {
            "value": ws.index(*_area_to_search[0]),  # ie, the value at area start position
            "location": copy.deepcopy(_area_to_search),
        }
    }
    #
    # find customer key "CUI / Registration ID" ==> `param_invoice_header_area...[CUI]` && `Invoice...[cbc_CompanyID]`
    _temp_found_data = get_excel_data_at_label(
        pattern_to_search_for=PATTERN_FOR_PARTNER_ID,
        worksheet=ws,
        area_to_scan=_area_to_search,
        targeted_type=str,
        down_search_try=False  # customer area is supposed to be organized as "label & value @ RIGHT" or "label: value @ IN-LABEL" but never @ DOWN as being a "not-a-practiced-natural-way"
    )  # returned info: `{"value": ..., "location": (row..., col...)}`
    param_invoice_header_area[unif_partner_area_key]["CUI"] = {
        "value": _temp_found_data["value"],
        "location": _temp_found_data["location"],
        "label_value": _temp_found_data["label_value"],
        "label_location": _temp_found_data["label_location"]
    }
    #
    # find customer key "RegistrationName" ==> `cbc_RegistrationName`
    '''#NOTE: `ReNaSt`-RegNameStrategy (remark: step codes will referred as defined here)
          ReNaSt.STEP-1. search for UNIF_PATTERN_FOR_PARTNER_LEGAL_NAME  #FIXME constant adjusted in refactoring process
          ReNaSt.STEP-2. if `label_location` of FOUND VALUE has the same location as `param_invoice_header_area[unif_partner_area_key]["area_info"]["location"][0]`:
                             keep VALUE of FOUND info
          ReNaSt.STEP-3. else:
                             keep `param_invoice_header_area[unif_partner_area_key]["area_info"]["value"]`
    '''
    _temp_found_data = get_excel_data_at_label(  # NOTE: ReNaSt.STEP-1
        pattern_to_search_for=UNIF_PATTERN_FOR_PARTNER_LEGAL_NAME,  #FIXME constant adjusted in refactoring process
        worksheet=ws,
        area_to_scan=_area_to_search,
        targeted_type=str,
        down_search_try=True  # NOTE: set on True to obtain identical results as original search of `PATTERN_FOR_INVOICE_CUSTOMER_SUBTABLE_MARKER` because name is supposed to be in a very "unstructured mode"
    )  # returned info: `{"value": ..., "location": (row..., col...)}`
    _location_of_header_partner_area = param_invoice_header_area[unif_partner_area_key]["area_info"]["location"][0]
    _location_of_value_found = _temp_found_data["label_location"]
    if _location_of_value_found == _location_of_header_partner_area:  # NOTE: ReNaSt.STEP-2
        kept_RegistrationName = _temp_found_data["value"]
        kept_RegistrationName_location = _temp_found_data["location"]
    else:  # NOTE: ReNaSt.STEP-3
        kept_RegistrationName = param_invoice_header_area[unif_partner_area_key]["area_info"]["value"]
        kept_RegistrationName_location = param_invoice_header_area[unif_partner_area_key]["area_info"]["location"][0]
    param_invoice_header_area[unif_partner_area_key]["RegistrationName"] = {
        "value": kept_RegistrationName,
        "location": kept_RegistrationName_location,
        "label_value": "n/a",
        "label_location": "n/a"
    }
    #
    # find customer key `cac:PostalAddress` -> `param_invoice_header_area["cac_PostalAddress"]` && Invoice...["cac_PostalAddress"]
    _temp_found_data = get_excel_data_at_label(
        pattern_to_search_for=PATTERN_FOR_PARTNER_ADDRESS,
        worksheet=ws,
        area_to_scan=_area_to_search,
        targeted_type=str,
        down_search_try=False  # customer area is supposed to be organized as "label & value @ RIGHT" or "label: value @ IN-LABEL" but never @ DOWN as being a "not-a-practiced-natural-way"
    )  # returned info: `{"value": ..., "location": (row..., col...)}`
    _tmpstr = _temp_found_data["label_value"].lower()
    _val_is_full_addr = ("adr" in _tmpstr) or ("addr" in _tmpstr)
    if _val_is_full_addr:
        area_to_scan_address_items = (_temp_found_data["location"], _temp_found_data["location"])
    else:
        area_to_scan_address_items = _area_to_search
    search_address_parts = partial(  # define a partial function to be used for all address items search
        get_excel_data_at_label,  # function to call
        worksheet=ws,
        area_to_scan=area_to_scan_address_items,
        targeted_type=str,
        down_search_try=False  # customer area is supposed to be organized as "label & value @ RIGHT" or "label: value @ IN-LABEL" but never @ DOWN as being a "not-a-practiced-natural-way"
    )  # returned info: `{"value": ..., "location": (row..., col...)}`
    _tmp_country = str(search_address_parts(pattern_to_search_for=PATTERN_FOR_PARTNER_ADDRESS_COUNTRY)["value"]).replace("None", "").strip()
    _tmp_city = str(search_address_parts(pattern_to_search_for=PATTERN_FOR_PARTNER_ADDRESS_CITY)["value"]).replace("None", "").strip()
    _tmp_street = str(search_address_parts(pattern_to_search_for=PATTERN_FOR_PARTNER_ADDRESS_STREET)["value"]).replace("None", "").strip()
    _tmp_zipcode = str(search_address_parts(pattern_to_search_for=PATTERN_FOR_PARTNER_ADDRESS_ZIPCODE)["value"]).replace("None", "").strip()
    if (_tmp_country is None) or (_tmp_country == ""):
        _tmp_country = UNIF_DEFAULT_PARTNER_COUNTRY  #FIXME constant adjusted in refactoring process
    else:  # update default value to be re-used in other parts if neccesary. Update is made on original variables "global" defined
        if partner_type == "CUSTOMER":
            DEFAULT_CUSTOMER_COUNTRY = _tmp_country  #FIXME constant adjusted in refactoring process
        else:  # case of "SUPPLIER" and "OWNER"
            DEFAULT_SUPPLIER_COUNTRY = _tmp_country  #FIXME constant adjusted in refactoring process
    param_invoice_header_area[unif_partner_area_key]["PostalAddress"] = {
        "cbc_StreetName": _tmp_street,
        "cbc_CityName": _tmp_city,
        "cbc_PostalZone": _tmp_zipcode,
        "cac_Country": {"cbc_IdentificationCode": _tmp_country},
    }
    #
    # find / search_extended_parts: rest of keys, like: "reg com", "bank / IBAN / cont", "tel", "email" (in code will use names like this: "search_extended_parts")*
    search_extended_parts = partial(  # define a partial function to be used for all "search_extended_parts"
        get_excel_data_at_label,  # function to call
        worksheet=ws,
        area_to_scan=_area_to_search,  # supposed to still contain customer info found area
        targeted_type=str,
        down_search_try=False  # customer area is supposed to be organized as "label & value @ RIGHT" or "label: value @ IN-LABEL" but never @ DOWN as being a "not-a-practiced-natural-way"
    )  # returned info: `{"value": ..., "location": (row..., col...)}`
    _tmp_reg_com = search_extended_parts(pattern_to_search_for=PATTERN_FOR_PARTNER_REGCOM)
    _tmp_bank = search_extended_parts(pattern_to_search_for=PATTERN_FOR_PARTNER_BANK)
    _tmp_IBAN = search_extended_parts(pattern_to_search_for=PATTERN_FOR_PARTNER_IBAN)
    _tmp_phone = search_extended_parts(pattern_to_search_for=PATTERN_FOR_PARTNER_TEL)
    _tmp_email = search_extended_parts(pattern_to_search_for=PATTERN_FOR_PARTNER_EMAIL)
    # store "full" variables in `customer_area...` for excel original values
    param_invoice_header_area[unif_partner_area_key]["reg_com"] = _tmp_reg_com
    param_invoice_header_area[unif_partner_area_key]["bank"] = _tmp_bank
    param_invoice_header_area[unif_partner_area_key]["IBAN"] = _tmp_IBAN
    param_invoice_header_area[unif_partner_area_key]["phone"] = _tmp_phone
    param_invoice_header_area[unif_partner_area_key]["email"] = _tmp_email


    # TODO: see how replicate code for Customer --to--> Supplier


    pass  # exit that normally should be unreachable





# TEST AREA
if __name__ == "__main__":
    get_partner_data()

