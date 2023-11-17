#!./.wenv_xl2roefact/bin/python3
"""  RDINV - modul de procesare a fisierului format XLSX ce contine factura si colectare a datelor aferente

    Identification:
        code-name: `rdinv`
        copyright: (c) 2023 RENWare Software Systems
        author: Petre Iordanescu (petre.iordanescu@gmail.com)

    Specifications:
        document: `110-SRE-api_to_roefact_requirements.md` section `Componenta xl2roefact`
        INTRARI: fisier format XLSX ce contine factura emisa (cod: `f-XLSX`)
        IESIRI: fisier format JSON imagine a datelor facturii (cod: `f-JSON`)
"""

# general modules (should be already imported by BaseProc class)
from datetime import datetime
from colorama import Fore, Back, Style
import copy
from pprint import pprint

# specific modules
import pylightxl as xl
import openpyxl as oxl

# constants
SYS_FILLED_EMPTY_CELL = "___sys_filled_empty_cell" #TODO subject of CONFIG



def rdinv(file_to_process: str, invoice_worksheet_name: str = None):
    """ main function of RDINV module

    Arguments:
        - `file_to_process`: the invoice file (exact file with path)
        - `invoice_worksheet_name`: the worksheet containing invoice

    Return:
        - tuple of `(invoice_header_area: dict, invoice_items_area: dict, invoice_footer_area: dict)`

    Important variables:
        - `db`: htxl object with invoice EXCEL (as a whole)
        - `ws`: pylightxl object with invoice WORKSHEET
    """

    print(f"\n*** Module {Fore.CYAN} RDINV (code-name: `rdinv`){Style.RESET_ALL} started at {Fore.GREEN}{datetime.now()}{Style.RESET_ALL} to process file {Fore.GREEN} {file_to_process}{Style.RESET_ALL}")

    # read Excel file with Invoice data
    try:
        db = xl.readxl(fn=file_to_process)
    except:
        print(f"{Fore.RED}***FATAL ERROR - Cannot open Excel file {file_to_process} (possible problems: file corrupted, wrong type only XLSX accetpted, file does not exists or was deleted, operating system vilotation) in Module {Fore.RED} RDINV (code-name: `rdinv`). File processing terminated{Style.RESET_ALL}")
        return False
    #print(f"{Fore.YELLOW}DEBUG-note:{Style.RESET_ALL} `rdinv` module, Excel database read (`db` variable) as: {db}{Style.RESET_ALL}") #NOTE for debug purposes

    # read the workshetd with Invoice data
    if invoice_worksheet_name is None: # if parameter `invoice_worksheet_name` not specified try to open first worksheet from Excel worksheets - order is given by worksheets order in Excel file
        list_of_excel_worksheets = db.ws_names
        print(f"{Fore.YELLOW}INFO note:{Style.RESET_ALL} `rdinv` module, no worksheet specified so will open first from this list {list_of_excel_worksheets}")
        invoice_worksheet_name = list_of_excel_worksheets[0]

    try:
        ws = db.ws(invoice_worksheet_name)
    except:
        print(f"{Fore.RED}***FATAL ERROR - Cannot open Excel specified Worksheet \"{invoice_worksheet_name}\" in Module {Fore.RED} RDINV (code-name: `rdinv`). File processing terminated{Style.RESET_ALL}")
        return False
    #print(f"{Fore.YELLOW}DEBUG-note:{Style.RESET_ALL} `rdinv` module, Excel worksheet read (`ws` variable) as: {ws}{Style.RESET_ALL}") #NOTE for debug purposes

    #
    # detect all cells that should be changed to SYS_FILLED_EMPTY_CELL (these are cells id merged groups where first cell in merged group is relevant (diff from empty))
    detected_cells_which_will_be_fake_filled = _get_merged_cells_tobe_changed(file_to_process, invoice_worksheet_name)
    #print(f"----------DETECTED RANGES: {detected_cells_which_will_be_fake_filled}") #NOTE for debug purposes
    # scan all detectected cell and change them
    for _cell_index in detected_cells_which_will_be_fake_filled:
        _cell_row = _cell_index[0]
        _cell_col = _cell_index[1]
        ws.update_index(row = _cell_row, col = _cell_col, val = SYS_FILLED_EMPTY_CELL)



    """ #NOTE section `invoice_items_area` to scan invoice to process `invoice_items_area`
        - Description:
            - find invoice items subtable
            - clean invoice items subtable
            - extract relevenat data
        - Return / generate: `invoice_items_area`
        - Notes:
            - to find invoice items subtable, code search for keyword defined in `keyword_for_items_table_marker`
            - normally this 'marker' will vary from invoice to invoice but usual cases contain strings 'crt', 'no', 'nr'
                - search for a cell that contains any combination of that 'potential markers'
                - consider for case insensitive and without punctuation symbols)
        - section ends with comment "------ END OF section `invoice_items_area`"
        - MASTER PLAN:
            - [x] variable names for zones: `invoice_header_area`, `invoice_items_area`, `invoice_footer_area`
            - [x] detected `invoice_items_area`
            - [x] clean `invoice_items_area` &
            - [x] preserved rows index in a separated structure (`invoice_items_area["keyrows_index"]`) & updated corresponding `del <keyrows>` to maintain it
            - [...#FIXME... GRESIT PTR CA TREBUIE INDEXUL REAL AL LINIEI, NU RELATIV LA `ssd`] improve search of `keyword_for_items_table_marker` (search the cell containg text fragments --> get text from that cell --> use it as `ssd()` parameter)
            - [ ] #TODO transform `invoice_items_area` (dataset format) to `invoice_items_area_JSON` (JSON format)
    """
    # string-markers to search for to isolate `invoice_items_area` (#NOTE partial END result: `_found_cell = (row, col, val)`)
    _ws_max_rows, _ws_max_cols = ws.size[0], ws.size[1]
    _FOUND_RELEVANT_CELL = False
    for _crt_row in range(1, _ws_max_rows + 1): # traverse all rows (start from 1 as Excel style)
        for _crt_col in range(1, _ws_max_cols + 1): # traverse all cols (start from 1 as Excel style)
            _crt_cell_val = ws.index(_crt_row, _crt_col)
            if (_crt_cell_val == "") or (_crt_cell_val == "___sys_filled_empty_cell") or (_crt_cell_val is None): # skip empty cells and continue with next cells
                continue
            # search ONLY STRINGS for ["crt", "no.", "nr."] / if not sjkip to next cell
            _cell_val_to_test = str(_crt_cell_val).lower()
            if (" crt" in _cell_val_to_test) or ("#" in _cell_val_to_test):
                _found_cell = (_crt_row, _crt_col, _crt_cell_val)
                _FOUND_RELEVANT_CELL = True
            else:
                continue
            if _FOUND_RELEVANT_CELL: # if found a relevant cell then exit
                break
        if _FOUND_RELEVANT_CELL: # if found a relevant cell then exit
            break
    if not _FOUND_RELEVANT_CELL:
        print(f"{Fore.RED}***FATAL ERROR - Cannot find a relevant cell where invoice items table start (basically containing string \" crt\"). File processing terminated{Style.RESET_ALL}")
        return False
    keyword_for_items_table_marker = _found_cell[2] #NOTE here you have `_found_cell = (row, col, val)` so set variable `keyword_for_items_table_marker`

    # obtain table with invoice items ==> `invoice_items_area`
    invoice_items_area = ws.ssd(keycols = keyword_for_items_table_marker, keyrows = keyword_for_items_table_marker)
    if (invoice_items_area is None or ((isinstance(invoice_items_area, list)) and len(invoice_items_area) < 1)): # there was not detected any area candidate to "invoice items / lines", so will exit rasing error
        print(f"{Fore.RED}***FATAL ERROR - Cannot find any candidate to for invoice ITEMS. Worksheet - \"{invoice_worksheet_name}\" in Module {Fore.RED} RDINV (code-name: `rdinv`). File processing terminated{Style.RESET_ALL}")
        return False

    #TODO test if list has more items (ie, that means more item tables that will need to be consolidated)
    if isinstance(invoice_items_area, list) and len(invoice_items_area) > 0:
        #   #NOTE `invoice_items_area` dictionary with keys: "keyrows", "keycols" and "data" (self explanatory)
        invoice_items_area = invoice_items_area[0] #NOTE NOW will suppose found just one AND retain only first one (index [0]) - SEE AFTER TEST with RENware invoice...

    """ CLEANING & CLEARING section """
    # clean full empty rows & preserve actual rows index in a separated structure (`invoice_items_area["keyrows_index"]`)
    invoice_items_area["keyrows_index"] = list()
    for _tmp_row_index, _tmp_row in enumerate(invoice_items_area["keyrows"]): # scan all rows and those with empty name/title are first candidates
        invoice_items_area["keyrows_index"].append(_tmp_row_index) #FIXME_#FIXME_#FIXME GRESIT PTR CA TREBUIE INDEXUL REAL AL LINIEI, NU RELATIV LA `ssd`
        if _tmp_row == SYS_FILLED_EMPTY_CELL:
            # inspect all row cells to see if all are empty (aid: `row(row, formula=False, output='v')`)
            _tmp_test_row_if_full_zero = sum([0 if _i == SYS_FILLED_EMPTY_CELL else 1 for _i in invoice_items_area["data"][_tmp_row_index]])
            if _tmp_test_row_if_full_zero == 0: # efectivelly delete in subject objects
                del invoice_items_area["keyrows"][_tmp_row_index] # drop that row from "keyrows" keyword list
                # del invoice_items_area["keyrows_index"][_tmp_row_index] # drop that row from "keyrows" keyword list #NOTE there is no need, you just enumerated this index and dropeed it in the same for-loop step
                del invoice_items_area["data"][_tmp_row_index]  # drop that row from "data" keyword list

    # clean empty columns: columns without a name will be completly dropped as they are unusable anyway (ie, do not know what to do with them...)
    _tmp_cells_to_drop_in_data_key = list()
    _tmp_items_to_drop_in_keycols_key = list()
    for _tmp_col_index, _tmp_col in enumerate(invoice_items_area["keycols"]): # scan all cols and those with empty name/title are first candidates
        if _tmp_col == SYS_FILLED_EMPTY_CELL:
            # inspect all col cells to see if all are empty (aid: `col(col, formula=False, output='v')`)
            # efectivelly delete in subject objects
            _tmp_items_to_drop_in_keycols_key.append(_tmp_col_index)
            for _data_row_index, _data_row in enumerate(invoice_items_area["data"]): # scan all rows to find out cells that are part of in subject columns
                # find out DATA all cells that corresponding to columns to be dropped ==> `_tmp_cells_to_drop_in_data_key: list[(row, col)]`
                _tmp_tmp = (_data_row_index, _tmp_col_index)
                _tmp_cells_to_drop_in_data_key.append(_tmp_tmp)
    # drop collected objects (column heads from KEYCOLS & correcsponding cell from DATA)
    for _obj_to_delete in reversed(_tmp_items_to_drop_in_keycols_key): # from KEYCOLS... (start with last item to not remain "in air" due to deletions :))
        del invoice_items_area["keycols"][_obj_to_delete]
    for _object_to_delete in reversed(_tmp_cells_to_drop_in_data_key): # from DATA... (start with last item to not remain "in air" due to deletions :))
        del invoice_items_area["data"][_object_to_delete[0]][_object_to_delete[1]]  # drop that col from "data" keyword list



    #TODO ...hereuare...
    ''' #NOTE___<<< quick action plan then come back to **line 80 PLAN** >>>___#NOTE
        - [ ] scan rows and and for thoses where are "rows between (ie, the index between 2 consecutive rows is > 1)" (index is in `invoice_items_area["keyrows_index"]`)
              scan description column to find more text that will become "extended description" (example for Kraftlangen invoice is text "SES 8105685514")
        - [ ] refactor `"keycols"` as:
            - actual value becomes --> `name_displayable`
            - map with an invoice real fields as `name`
        - [ ] see if keep next CLEANING steps
    '''

    ''' #FIXME_#FIXME uncomment up to finish task: "clean full empty columns" --(up to text "END of uncommenta area")
    # if first column is empty then set it to `keyword_for_items_table_marker` (as is the only reasonable possibility of "invoice layout format")
    if len(invoice_items_area["keycols"]) < 1: # this code should never be entered - probably is a system error
        print(f"{Fore.RED}***SYSTEM ERROR - Invoice items subtable does not have any columns. Worksheet - \"{invoice_worksheet_name}\" in Module {Fore.RED} RDINV (code-name: `rdinv`). File processing terminated{Style.RESET_ALL}")
        return False
    if invoice_items_area["keycols"][0] == SYS_FILLED_EMPTY_CELL:
        invoice_items_area["keycols"][0] = keyword_for_items_table_marker
    '''

    ''' # #TODO set back to empty cells that remained to `SYS_FILLED_EMPTY_CELL`
    invoice_items_area["keycols"] = ["" if _i == SYS_FILLED_EMPTY_CELL else _i for _i in invoice_items_area["keycols"]] # loop for 'keycols' keyword
    invoice_items_area["keyrows"] = ["" if _i == SYS_FILLED_EMPTY_CELL else _i for _i in invoice_items_area["keyrows"]] # loop for 'keyrows' keyword
    for _tmp_row_index, _tmp_row in enumerate(invoice_items_area["data"]): # # loop for 'data' keyword (first loop table rows, "data" key is matrix of lines & cells, ie as [][])
        _tmp_row = ["" if _i == SYS_FILLED_EMPTY_CELL else _i for _i in _tmp_row]
        invoice_items_area["data"][_tmp_row_index] = _tmp_row
    '''

    # #TODO_nxt_atep identify relevant data and write to file `f-JSON` (factura emisa in format JSON intermediar pentru generare - vezi documentatia)

    ''' #FIXME ---------------------------- END of uncommenta area

    '''#===============================================================================
    # #NOTE ------ END OF section `invoice_items_area`
    #==============================================================================='''







    #FIXME test area & notes starts here
    print(f"{Fore.YELLOW}---> TEST-note: sub-tabel[0], factura contine:{Style.RESET_ALL}") #NOTE test should be an array of arrays (matrix) with invoice items #FIXME drop after test
    pprint(invoice_items_area, width = 132) #FIXME drop after test
    print()
    '''
    #NOTE rezultat obtinut __RENware invoice__: "---> TEST-note: ssub-tabel[0],.. sub-tabel[0], factura contine: ..."
        {
                'data': [
                    [1, 2, 3, 4, '5 = 3 x 4', '6 = 5 x 19%'],
                    ['Elaborare documentatie tehnica aplicatie NEXGEN.AI', 'buc', 1, 14807.4, 14807.4, 2813.41]
                ],
                'keycols': ['Denumirea produselor sau a serviciilor',
                            'UM',
                            'Cant.',
                            'Pret unitar\n(fara TVA)\n- RON -',
                            'Valoarea\n(fara TVA)\n- RON -',
                            'TVA\n- RON -'],
                'keyrows': ['0', 1],
                'keyrows_index': [0, 1]
        }
    #NOTE rezultat obtinut __Kraftlangen invoice__: "---> TEST-note:  sub-tabel[0], factura contine: ..."
        {
            'data': [
                ['Inlocuit conducta PSI coloana C2 DAV.', 1, 42756.08, 0.19, 42756.08, 8123.6552]
            ],
            'keycols': ['Denumirea lucrarii                                  (Request description)',
                        'Cantitatea (Quantity)',
                        'Pret unitar (Unit price)',
                        'Cota TVA (VAT %)',
                        'Valoare fara TVA (Value without VAT)',
                        'Valoare TVA (Value VAT)'],
            'keyrows': [1],
            'keyrows_index': [0]
        }
    '''

    #NOTE result is: (`invoice_header_area`, `invoice_items_area`, `invoice_footer_area`)
    return (None, invoice_items_area, None) #FIXME update with the other zones whene ready












# #NOTE - ready, test PASS @ 231111 by [piu] #TODO NEED to be cleaned
def _get_merged_cells_tobe_changed(file_to_scan, invoice_worksheet_name):
    """ scan Excel file to detect all merged ranges

    Arguments:
        - `file_to_scan`: the excel file to be scanned
        - `invoice_worksheet_name`: the worksheet to be scanned
        - `only_cells_tobe_changed`: boolean indicating to

    Return:
        - `cells_to_be_changed`: list with cells that need to be chaged in format `(row,col)`

    Notes:
        - function is intended to be used ONLY internal in this module
        - use `openpyxl` library to do its job
    """

    all_detected_ranges = []
    # open Excel file
    workbook_oxl= oxl.load_workbook(file_to_scan)
    #print(f"\n==================== function `_get_merged_cells_tobe_changed()`, opened excel ==> {workbook_oxl}") #FIXME - test, drop me
    # open worksheet
    worksheet_oxl = workbook_oxl[invoice_worksheet_name] #FIXME seems useless because sheet is opened in next code lines DROP ME AND use name `worksheet_oxl` in line 179
    #print(f"==================== function `_get_merged_cells_tobe_changed()`, opened sheet ==> {worksheet_oxl}") #FIXME - test, drop me
    # get all merged ranges
    all_detected_ranges = worksheet_oxl.merged_cells.ranges
    #print(f"==================== function `_get_merged_cells_tobe_changed()`, merged ranges ==> {all_detected_ranges}") #FIXME - test, drop me
    _cells_to_be_changed = list() # will retaing cells that should be marked with SYS_FILLED_EMPTY_CELL
    for _crt_range in all_detected_ranges:
        # range coordinates
        #print(f"\n*** current range {_crt_range} with `size`: {_crt_range.size}, `bounds`: {_crt_range.bounds}") #FIXME drop me
        _crt_range_START_COL = _crt_range.bounds[0]
        _crt_range_END_COL = _crt_range.bounds[2]
        _crt_range_START_ROW = _crt_range.bounds[1]
        _crt_range_END_ROW = _crt_range.bounds[3]
        #print(f"\t/*** -start COL {_crt_range_START_COL} -end COL {_crt_range_END_COL} -start ROW {_crt_range_START_ROW} -end ROW {_crt_range_END_ROW}") #FIXME drop me
        # traversing range for all cells in
        _first_entry = True # if is first entry in rage traversing
        _full_break = False # if range is ireveant and need to leave & forget it
        for c in range(_crt_range_START_COL, _crt_range_END_COL + 1): # traverse all COLS ...
            for r in range(_crt_range_START_ROW, _crt_range_END_ROW + 1): # traverse all ROWS ...
                _crt_cell_value = worksheet_oxl.cell(r, c).value
                #print(f"\t/***** processing cell (row,col = {r},{c}) has value {_crt_cell_value}") # #FIXME drop me
                if _first_entry: # see if relevant (ie, not empty or empty string) AND if NOT then break all loops
                    if _crt_cell_value is None:
                        _full_break = True
                        break
                    if isinstance(_crt_cell_value, str) and _crt_cell_value.strip() == "": # clean cell value to see if remain empty
                        _full_break = True
                        break
                    #print(f"\t/***** RELEVANT cell (row,col = {r},{c}) has value {_crt_cell_value}") # #FIXME drop me
                if not _first_entry: # here the cell has a relevant value, store all next to be marked with SYS_FILLED_EMPTY_CELL
                    _cells_to_be_changed.append((r, c))
                    #print(f"\t/***** cell {(r, c)} marked for '___sys_filled_empty_cell' / {Fore.YELLOW}all list is {_cells_to_be_changed}{Style.RESET_ALL}") # #FIXME drop me
                _first_entry = False
            if _full_break:
                break
    return tuple(copy.deepcopy(_cells_to_be_changed)) # always return a tuple as being immutable



