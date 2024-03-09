#!../.venv/bin/python3
"""general utilities library for all `xl2roefact` components and modules.

Identification:

* code-name: `libutils`
* copyright: (c) 2023, 2024 RENWare Software Systems
* author: Petre Iordanescu (petre.iordanescu@gmail.com)

Components:

* `complete_sexe_file() -> bool`: Rename and move resulted exe file (called from `build_sexe` script)
* `dict_sum_by_key(dict, str) -> float`: Sum a dictionary for a given key at all depth levels
* `find_str_in_list(list, list) -> int`: Search more strings (ie, a list) in list of strings
* `invoice_taxes_summary(list[dict]) -> dict`: Calculates invoice taxes summary as required by ROefact requirements
* `isnumber(str) -> bool`: Test a string if it could be used as number (int or float)

"""

import sys
from rich import print
from fractions import Fraction
import copy


# NOTE: in tests @240309T1600
from xl2roefact.__version__ import normalized_version
from pathlib import Path
def complete_sexe_file() -> bool:
    """Rename and move resulted exe file. This function is dedicated only to development phase, so various objects are hard coded.

    Specs: file to process `.../dist_sexe/xl2roefact_to_update_name.exe` --> `.../dist/xl2roefact-version-win64.exe

    Return:
        `bool`: True if file was found, renamed and moved with no error
    """
    # NOTE: all function suppose that current directory is where xl2roefact package "start"
    process_stat = True
    # get canonical version string
    canonical_version = str(normalized_version())
    # construct a Path() type for source
    source_file = Path("./dist_sexe/xl2roefact_to_update_name.exe")
    # construct a Path() type for for destination
    dest_file = Path(f"./dist/xl2roefact-{canonical_version}-win64.exe")
    print(f"******\n--- {source_file=}\n--- {dest_file=}\n--- {canonical_version=}")  #FIXME dbg drop me
    # mv source file to dest using new name. If destination exists is replaced
    tstdst = bool(dest_file.is_file() and dest_file.exists())
    tstsrc = bool(source_file.is_file() and source_file.exists())
    print(f"******Test results\n---{tstsrc=}\n---{tstdst=}")  #FIXME dbg can drop
    if not tstsrc:  # we have no work object. exit with False
        return False
    if tstdst:  # drop destination file
        dest_file.unlink()
    # move source to destination
    op_result = source_file.rename(dest_file)
    print(f"******Move oper returned\n--- {op_result=}")  #FIXME dbg drop me   
    process_stat = bool(op_result)
    return process_stat







# NOTE: ready, unit test PASS @240305
def invoice_taxes_summary(
    invoice_lines: list[dict]
) -> list:
    """Calculates invoice taxes summary as required by ROefact requirements.

    Args:
        `invoice_lines`: section with item lines from 'big' invoice dictionary

    Return:
        `list`: usable for "cac_TaxSubtotal" key
    """
    copyof_invoice_lines = copy.deepcopy(invoice_lines)[0]  # make a copy and keep only real-effective list (first item of)
    tmp_InvoiceLine_dict = dict()
    tmpCompondedVAT_list = list()  # intended to keep found `VAT_types-Percent` combinations (ie, to do opera SQL-UPSERT like)
    for item_info in copyof_invoice_lines:
        req_item_info = dict()
        req_item_info["cbc_TaxableAmount"] = item_info.get("cbc_LineExtensionAmount", 0)
        req_item_info["cbc_TaxAmount"] = item_info.get("LineVatAmount", 0)
        work_cac_item = item_info.get("cac_Item")  # get first level as `dict`
        del work_cac_item["cbc_Name"]  # drop not neede information
        # temporary make a new compounded key as helper to GROUP the values by it (SQL GROUP BY like)
        req_item_info["cac_TaxCategory"] = work_cac_item
        tmpCompondedVAT = work_cac_item.get("cac_ClassifiedTaxCategory", dict())  # default return an empty dictionary
        tmpCompondedVAT_1 = str(tmpCompondedVAT.get("cbc_Percent"))
        tmpCompondedVAT_2 = str(tmpCompondedVAT.get("cac_TaxScheme").get("cbc_ID"))
        tmpCompondedVAT = tmpCompondedVAT_1 + tmpCompondedVAT_2
        #NOTE: acesta este hard coded in `xl2roefact`. Nu se va face mai mult de atit, variante cu alte TaxCategory fiind pentru un alt ERP  #TODO subject of documentation update
        req_item_info["cac_TaxCategory"]["ID"] = "S"  # NOTE: hard coded. see previous comment
        # next calc do SQL-UPSERT operation like
        if tmpCompondedVAT in tmpCompondedVAT_list:  # this info already exists, so adjust info for SQL-UPSERT like operation
            _prev_cbc_TaxableAmount = tmp_InvoiceLine_dict[tmpCompondedVAT]["cbc_TaxableAmount"]
            _prev_cbc_TaxAmount = tmp_InvoiceLine_dict[tmpCompondedVAT]["cbc_TaxAmount"]
            _actual_cbc_TaxableAmount = req_item_info["cbc_TaxableAmount"]
            _actual_cbc_TaxAmount = req_item_info["cbc_TaxAmount"]
            if (_actual_cbc_TaxableAmount is None) or (_prev_cbc_TaxableAmount is None):  # let unchanged (as was)
                req_item_info["cbc_TaxableAmount"] = _prev_cbc_TaxableAmount
            else:  # add with prev value
                req_item_info["cbc_TaxableAmount"] = _actual_cbc_TaxableAmount + _prev_cbc_TaxableAmount
            if (_actual_cbc_TaxAmount is None) or (_prev_cbc_TaxAmount is None):  # let unchanged (as was)
                req_item_info["cbc_TaxAmount"] = _prev_cbc_TaxAmount
            else:  # add with prev value
                req_item_info["cbc_TaxAmount"] = _actual_cbc_TaxableAmount + _prev_cbc_TaxAmount
        else:
            tmpCompondedVAT_list.append(tmpCompondedVAT)  # mark it as found
        tmp_InvoiceLine_dict[tmpCompondedVAT] = req_item_info
    # extract values of 1st level keys and preserve as list
    tmp_InvoiceLine_list = [tmp_InvoiceLine_dict[i] for i in tmp_InvoiceLine_dict]  # keep only values of "CompondedVAT" constructed keys
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
        `float`: with required sum
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
