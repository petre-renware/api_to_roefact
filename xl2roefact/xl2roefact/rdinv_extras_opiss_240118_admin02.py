
def get_partner_info(
    partner_type: str # TODO: one of "customer" | "supplier"
) -> dict:  #FIXME check if return is realy dict...
    """Summary here... .

    Extended info here... .

    Args:
        ...
    Return:
        ...
    """
    #FIXME_FIXME: >>>------------------[opiss `240118_admin02`]----- FROM here = point to make a function `get_partner_info(partner_type: str "customer" | "supplier")`
    # find invoice customer ==> "cac:AccountingCustomerParty
    invoice_customer_info = get_excel_data_at_label(
        pattern_to_search_for=PATTERN_FOR_INVOICE_CUSTOMER_SUBTABLE_MARKER,
        worksheet=ws,
        area_to_scan=(invoice_header_area["start_cell"], invoice_header_area["end_cell"]),
        targeted_type=str
    )  # returned info: `{"value": ..., "location": (row..., col...)}`
    # set a dedicated AREAs TO SEARCH for customer
    _area_to_search_start_cell = [  # use `label_location` as being supposed "most far away" from effective-good info, so more chances to find info
        0 if invoice_customer_info["label_location"][0] <= 0 else invoice_customer_info["label_location"][0] - 1,  # set one line up if this line exists
        invoice_customer_info["label_location"][1],
    ]
    if ws.index(*_area_to_search_start_cell).strip() == "":  # prev set was for one line up but if that cell is blank remake it (ie, do a +1)
        _area_to_search_start_cell[0] += 1
    # from `_area_to_search_start_cell` go down up a blank (empty cell)
    _last_ok_position = list([0, 0])
    for __i in range(_area_to_search_start_cell[0], ws.size[0] + 1):  # scan rest of lines for a blank one
        _crt_scanned_cell_idx = (__i, _area_to_search_start_cell[1])
        _crt_scanned_cell_val = ws.index(*_crt_scanned_cell_idx)
        if _crt_scanned_cell_val.strip() == "":  # here you must stop
            break
        # save current position to be used after break
        _last_ok_position = copy.deepcopy(_crt_scanned_cell_idx)
    _area_to_search_end_cell = [
        _last_ok_position[0],
        ws.size[1] if _last_ok_position[1] > ws.size[1] else _last_ok_position[1] + 1,  # set one row right if this row exists
    ]
    # set-persist `_area_to_search` for next steps & save its key-info in associated invoice JSON (for further references)
    _area_to_search = (tuple(_area_to_search_start_cell), tuple(_area_to_search_end_cell))
    invoice_header_area["customer_area"] = {
        "area_info": {
            "value": ws.index(*_area_to_search[0]),  # ie, the value at area start position
            "location": copy.deepcopy(_area_to_search),
        }
    }
    #
    # find customer key "CUI / Registration ID" ==> `invoice_header_area...[CUI]` && `Invoice...[cbc_CompanyID]`
    _temp_found_data = get_excel_data_at_label(
        pattern_to_search_for=PATTERN_FOR_PARTNER_ID,
        worksheet=ws,
        area_to_scan=_area_to_search,
        targeted_type=str,
        down_search_try=False  # customer area is supposed to be organized as "label & value @ RIGHT" or "label: value @ IN-LABEL" but never @ DOWN as being a "not-a-practiced-natural-way"
    )  # returned info: `{"value": ..., "location": (row..., col...)}`
    invoice_header_area["customer_area"]["CUI"] = {
        "value": _temp_found_data["value"],
        "location": _temp_found_data["location"],
        "label_value": _temp_found_data["label_value"],
        "label_location": _temp_found_data["label_location"]
    }
    #
    # find customer key "RegistrationName" ==> `cbc_RegistrationName`
    '''#NOTE: `ReNaSt`-RegNameStrategy (remark: step codes will referred as defined here)
          ReNaSt.STEP-1. search for PATTERN_FOR_CUSTOMER_LEGAL_NAME
          ReNaSt.STEP-2. if `label_location` of FOUND VALUE has the same location as `invoice_header_area["customer_area"]["area_info"]["location"][0]`:
                             keep VALUE of FOUND info
          ReNaSt.STEP-3. else:
                             keep `invoice_header_area["customer_area"]["area_info"]["value"]`
    '''
    _temp_found_data = get_excel_data_at_label(  # NOTE: ReNaSt.STEP-1
        pattern_to_search_for=PATTERN_FOR_CUSTOMER_LEGAL_NAME,
        worksheet=ws,
        area_to_scan=_area_to_search,
        targeted_type=str,
        down_search_try=True  # NOTE: set on True to obtain identical results as original search of `PATTERN_FOR_INVOICE_CUSTOMER_SUBTABLE_MARKER` because name is supposed to be in a very "unstructured mode"
    )  # returned info: `{"value": ..., "location": (row..., col...)}`
    _location_of_header_partner_area = invoice_header_area["customer_area"]["area_info"]["location"][0]
    _location_of_value_found = _temp_found_data["label_location"]
    if _location_of_value_found == _location_of_header_partner_area:  # NOTE: ReNaSt.STEP-2
        kept_RegistrationName = _temp_found_data["value"]
        kept_RegistrationName_location = _temp_found_data["location"]
    else:  # NOTE: ReNaSt.STEP-3
        kept_RegistrationName = invoice_header_area["customer_area"]["area_info"]["value"]
        kept_RegistrationName_location = invoice_header_area["customer_area"]["area_info"]["location"][0]
    invoice_header_area["customer_area"]["RegistrationName"] = {
        "value": kept_RegistrationName,
        "location": kept_RegistrationName_location,
        "label_value": "n/a",
        "label_location": "n/a"
    }
    #
    # find customer key `cac:PostalAddress` -> `invoice_header_area["cac_PostalAddress"]` && Invoice...["cac_PostalAddress"]
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
    )
    _tmp_country = str(search_address_parts(pattern_to_search_for=PATTERN_FOR_PARTNER_ADDRESS_COUNTRY)["value"]).replace("None", "").strip()
    _tmp_city = str(search_address_parts(pattern_to_search_for=PATTERN_FOR_PARTNER_ADDRESS_CITY)["value"]).replace("None", "").strip()
    _tmp_street = str(search_address_parts(pattern_to_search_for=PATTERN_FOR_PARTNER_ADDRESS_STREET)["value"]).replace("None", "").strip()
    _tmp_zipcode = str(search_address_parts(pattern_to_search_for=PATTERN_FOR_PARTNER_ADDRESS_ZIPCODE)["value"]).replace("None", "").strip()
    if (_tmp_country is None) or (_tmp_country == ""):
        _tmp_country = DEFAULT_CUSTOMER_COUNTRY
    else:
        DEFAULT_CUSTOMER_COUNTRY = _tmp_country  # update deflaute value to be re-used in other parts if neccesary
    invoice_header_area["customer_area"]["PostalAddress"] = {
        "cbc_StreetName": _tmp_street,
        "cbc_CityName": _tmp_city,
        "cbc_PostalZone": _tmp_zipcode,
        "cac_Country": {"cbc_IdentificationCode": _tmp_country},
    }
    # TODO: ... continue with search for the rest of keys, like: "reg com", "bank / IBAN / cont", and more...
    ...

    return None  #FIXME see what should be returned or None because modified directly in multable parameters
    #FIXME_FIXME: <<<------------------[opiss `240118_admin02`]----- TO here = point to make a function `get_partner_info(partner_type: str "customer" | "supplier")`


