#!../.venv/bin/python3
"""general utilities library for all `xl2roefact` components and modules.

Identification:

* code-name: `libutils`
* copyright: (c) 2023, 2024 RENWare Software Systems
* author: Petre Iordanescu (petre.iordanescu@gmail.com)

Components:

* `dict_sum_by_key(dict, str) -> float`: Sum a dictionary for a given key at all depth levels
* `find_str_in_list(list, list) -> int`: Search more strings (ie, a list) in list of strings
* `invoice_taxes_summary(list[dict]) -> dict`: Calculates invoice taxes summary as required by ROefact requirements
* `isnumber(str) -> bool`: Test a string if it could be used as number (int or float)

"""

import sys
from rich import print
from fractions import Fraction
import copy


# NOTE: wip...
def invoice_taxes_summary(
    invoice_lines: list[dict]
) -> dict:
    """Calculates invoice taxes summary as required by ROefact requirements.

    Args:
        `invoice_lines`: section with item lines from 'big' invoice dictionary

    Return:
        `dict` with required structure
    """

    '''  #FIXME drop.me -- NOTE: STRUCTURA LA CARE TREBUIE SA AJUNGI
    <cac:TaxTotal>
        <cbc:TaxAmount currencyID="RON">190.00</cbc:TaxAmount>
        <cac:TaxSubtotal>
            <cbc:TaxableAmount currencyID="RON">1000.00</cbc:TaxableAmount>
            <cbc:TaxAmount currencyID="RON">190.00</cbc:TaxAmount>
            <cac:TaxCategory>
                <cbc:ID>S</cbc:ID>
                <cbc:Percent>19.00</cbc:Percent>
                <cac:TaxScheme>
                    <cbc:ID>VAT</cbc:ID>
                </cac:TaxScheme>
            </cac:TaxCategory>
        </cac:TaxSubtotal>
    </cac:TaxTotal>
    '''
    # make a copy and keep only and necessary keys
    copyof_invoice_lines = copy.deepcopy(invoice_lines)
    tmp_InvoiceLine_list = list()
    for item_info in copyof_invoice_lines[0]:  # keep only real-effective list
        req_item_info = dict()
        req_item_info["cbc_LineExtensionAmount"] = item_info.get("cbc_LineExtensionAmount", 0)
        req_item_info["LineVatAmount"] = item_info.get("LineVatAmount", 0)
        # to.get.pieces.of... ["cac_Item"]["cac_ClassifiedTaxCategory"]["cbc_Percent"]["cac_TaxScheme"]["cbc_ID"] == "VAT"
        work_cac_item = item_info.get("cac_Item")  # get first level as `dict`
        del work_cac_item["cbc_Name"]  # drop not neede information
        # get rest of structure from work_cac_item
        # ... and temporary make a new compounded key, helper to group the values by it
        req_item_info["cac_TaxCategory"] = work_cac_item
        tmpCompondedVAT = work_cac_item.get("cac_ClassifiedTaxCategory")
        tmpCompondedVAT_1 = str(tmpCompondedVAT.get("cbc_Percent"))
        tmpCompondedVAT_2 = str(tmpCompondedVAT.get("cac_TaxScheme").get("cbc_ID"))
        tmpCompondedVAT = tmpCompondedVAT_1 + tmpCompondedVAT_2
        req_item_info["tmpCompondedVAT"] = tmpCompondedVAT
        ''' #NOTE: kind of keys resulted (to see GROUP BY combinations)
            "tmpCompondedVAT": "0.19VAT"
            "tmpCompondedVAT": "NoneNone"
            "tmpCompondedVAT": "0.0VAT"
        '''  #NOTE: these are subject of GROUP BY sum
        # ... sum += (ExtAmnt ai VatAmnt) for this key
        # ... if exists should be updated.
        # ... if not take care to add with 0 as being first time when add it
        ''' #FIXME dbg can drop. INFORMATIA CREATA pina in acest punct este: :
        {
            "cbc_LineExtensionAmount": 38890.25,
            "LineVatAmount": 7389.15,
            "cac_TaxCategory": {
                "cac_ClassifiedTaxCategory": {
                    "cbc_Percent": 0.19,
                    "cac_TaxScheme": {
                        "cbc_ID": "VAT"
                    }
                },
                "ID": "S"
            }
        }
        '''  # si de verificat nivelul "cac_Item" care trebuie pastrat doar continutul sau, ie work_cac_item["cac_Item"]
        req_item_info["cac_TaxCategory"]["ID"] = "S"  # acesta este hard coded pentru `xl2roefact` - a face mai mult de atit poate un ERP #TODO subject of documentation update
        tmp_InvoiceLine_list.append(req_item_info)
    # ...??? build dict parts of final structure
    ...
    return tmp_InvoiceLine_list








# NOTE: ready, unit test PASS @240223
def dict_sum_by_key(
    search_dict: dict | list[dict],
    sum_key: str
) -> float:
    """Sum all dictionary (or list off dictionaries) items, at all levels, for a given key.

    Args:
        `search_dict`: dictionary to be searched for
        `sum_key`: key to be searched

    Return:
        `float` with required sum
    """
    s = 0
    if isinstance(search_dict, list) or isinstance(search_dict, tuple):
        for local_search_dict in search_dict:
            for k in local_search_dict:
                if isinstance(local_search_dict[k], dict):
                    s += dict_sum_by_key(local_search_dict[k], sum_key)
                if k == sum_key:
                    try: kval = int(local_search_dict[k])
                    except: kval = 0
                    s += kval
    else:
        for k in search_dict:
            if isinstance(search_dict[k], dict):
                s += dict_sum_by_key(search_dict[k], sum_key)
            if k == sum_key:
                try: kval = int(search_dict[k])
                except: kval = 0
                s += kval
    return float(s)




# NOTE: ready, test PASS @231123
def isnumber(a_string: str) -> bool:
    """test if a string is valid as any kind of number.

    Args:
        `a_string`: input string.

    Return:
        `True`: if input string is valid as any kind of number, orherwise `False`.
    """
    try:
        float(a_string)
        return True
    except ValueError:
        try:
            Fraction(a_string)
            return True
        except ValueError:
            return False



# NOTE: ready, test PASS @231123
def find_str_in_list(list_of_str_to_find: list, list_to_search: list) -> int:
    """find a substring from `list_of_str_to_find` in elements of `list_to_search`.

    Args:
        `list_of_str_to_find`: list of strings to search for.
        `list_to_search`: liste where to search for substrings.

    Return:
        `index`: the index of list item which contains `str_to_find` (first found) or `None` if not found.
    """
    __found = False
    for __crt_str_to_search_for in list_of_str_to_find:
        __tmp_list = [
            x.find(str(__crt_str_to_search_for))
            for i, x in enumerate(
                [x.lower().replace(".", "") for x in [str(x) for x in list_to_search]]
            )
        ]  # make it all items as lowercase string and drop all "." chars ... it is a long code line, seems hard but is just characters processing searchin for a string...
        try:
            _item_index = __tmp_list.index(
                False
            )  # col position has a False val in list
            __found = True
        except:  # did not find a suitable column to represent quantity, so return None probably raising an error
            continue
    return _item_index if __found else None
