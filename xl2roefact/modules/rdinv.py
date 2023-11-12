#!../.wenv_xl2roefact/bin/python3
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
SYS_FILLED_EMPTY_CELL = "___sys_filled_empty_cell" #TODO should be subject of CONFIG



def rdinv(file_to_process: str, invoice_data_worksheet: str = None):
    """ main function of RDINV module

    Arguments:
        - `file_to_process`: the invoice file (exact file with path)
        - `invoice_data_worksheet`: the worksheet containing invoice

    Return:
        - tuple of `(invoice_header_area: #FIXME_unknown_yet, invoice_lines_area: dict, invoice_footer_area: #FIXME_unknown_yet)`

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
    invoice_worksheet_name = invoice_data_worksheet
    if invoice_worksheet_name is None: # if parameter `invoice_data_worksheet` not specified try to open first worksheet from Excel worksheets - order is given by worksheets order in Excel file
        list_of_excel_worksheets = db.ws_names
        print(f"{Fore.YELLOW}INFO note:{Style.RESET_ALL} `rdinv` module, no worksheet specified so will open firts from this list {list_of_excel_worksheets}")
        invoice_worksheet_name = list_of_excel_worksheets[0]

    try:
        ws = db.ws(invoice_worksheet_name)
    except:
        print(f"{Fore.RED}***FATAL ERROR - Cannot open Excel specified Worksheet ({invoice_worksheet_name}) in Module {Fore.RED} RDINV (code-name: `rdinv`). File processing terminated{Style.RESET_ALL}")
        return False
    #print(f"{Fore.YELLOW}DEBUG-note:{Style.RESET_ALL} `rdinv` module, Excel worksheet read (`ws` variable) as: {ws}{Style.RESET_ALL}") #NOTE for debug purposes

    # -----------------
    # detect all cells that should be changed to SYS_FILLED_EMPTY_CELL (these are cells id merged groups where first cell in merged group is relevant (diff from empty))
    detected_cells_which_will_be_fake_filled = _get_merged_cells_tobe_changed(file_to_process, invoice_worksheet_name) # ...hereuare...
    #print(f"----------DETECTED RANGES: {detected_cells_which_will_be_fake_filled}") #FIXME drop me as debugging
    # scan all detectected cell and change them
    for _cell_index in detected_cells_which_will_be_fake_filled:
        _cell_row = _cell_index[0]
        _cell_col = _cell_index[1]
        ws.update_index(row = _cell_row, col = _cell_col, val = SYS_FILLED_EMPTY_CELL)
        #print(f"cell {_cell_index} updated. new read va is: {ws.index(row = _cell_row, col = _cell_col)}") #FIXME drop after test

    ''' #NOTE quick plan:
    - [x] detected `invoice_lines_area`
    - [ ] isolate header and footer after clean `invoice_lines_area`
    - [x] variable names for zones: `invoice_header_area`, `invoice_lines_area`, `invoice_footer_area`
    '''
    # -----------------
    # string-markers to search for to isolate `invoice_lines_area` #TODO to be unified (how? - search the cell containg text fragments --> get text from that cell --> use it as `ssd()` parameter)
    # #NOTE_ATT_README: tmp_items_table_marker_string = "crt" #FIXME drop me - DOES NOT WORK, search is exact... TRY THIS as "unified string"
    tmp_items_table_marker_string = "No. crt." #NOTE Kraftlangen invoice
    #tmp_items_table_marker_string = "Nr. crt" #NOTE RENware invoice

    # obtain table with invoice items ==> `invoice_lines_area`
    invoice_lines_area = ws.ssd(keycols = tmp_items_table_marker_string, keyrows = tmp_items_table_marker_string)
    if (invoice_lines_area is None or ((isinstance(invoice_lines_area, list)) and len(invoice_lines_area) < 1)): # there was not detected any area candidate to "invoice items / lines", so will exit rasing error
        print(f"{Fore.RED}***FATAL ERROR - Cannot find any candidate to for invoice ITEMS. Worksheet - ({invoice_data_worksheet}) in Module {Fore.RED} RDINV (code-name: `rdinv`). File processing terminated{Style.RESET_ALL}")
        return False

    #TODO test if list has more items (ie, that means more item tables that will need to be consolidated)
    if isinstance(invoice_lines_area, list) and len(invoice_lines_area) > 0:
        #NOTE `invoice_lines_area` dictionary with keys: "keyrows", "keycols" and "data" (self explanatory)
        invoice_lines_area = invoice_lines_area[0] #NOTE NOW will suppose is just one AND retain only first one (index [0]) - SEE AFTER TEST with RENware invoice...

    # -----------------
    # clean cells that contains `SYS_FILLED_EMPTY_CELL`
    for _i, _val in enumerate(invoice_lines_area["keycols"]): # loop for 'keycols' keyword
        invoice_lines_area["keycols"][_i] = "" if _val == SYS_FILLED_EMPTY_CELL else invoice_lines_area["keycols"][_i]
    for _i, _val in enumerate(invoice_lines_area["keyrows"]): # loop for 'keyrows' keyword
        invoice_lines_area["keyrows"][_i] = "" if _val == SYS_FILLED_EMPTY_CELL else invoice_lines_area["keyrows"][_i]
    for _tmp_row_index, _tmp_row in enumerate(invoice_lines_area["data"]): # # loop for 'data' keyword (first loop table rows, "data" key is matrix of lines & cells, ie as [][])
        for _i, _val in enumerate(_tmp_row):
            _tmp_row[_i] = "" if _val == SYS_FILLED_EMPTY_CELL else _tmp_row[_i]

    #TODO ...hereuare... @IMP==> need to clean empty rows

    #FIXME test area & notes starts here
    print(f"{Fore.YELLOW}---> TEST-note: tabel 0 linii factura contine:{Style.RESET_ALL}") #NOTE test should be an array of arrays (matrix) with invoice items #FIXME drop after test
    pprint(invoice_lines_area, width = 132) #FIXME drop after test
    print()

    '''#NOTE rezultat obtinut: "---> TEST-note: tabel 0 linii factura contine:...(nxt lines)..." #NOTE PASS OK for Kraftlangen invoice, only one line and data is OK
{
    'data': [
        ['', '', '', '', '', '', ''],
        ['Inlocuit conducta PSI coloana C2 DAV.', '', 1, 42756.08, 0.19, 42756.08, 8123.6552]
    ],
    'keycols': [
        'Denumirea lucrarii                                  (Request description)',
        '',
        'Cantitatea (Quantity)',
        'Pret unitar (Unit price)',
        'Cota TVA (VAT %)',
        'Valoare fara TVA (Value without VAT)',
        'Valoare TVA (Value VAT)'
    ],
    'keyrows': [
        '',
        1
    ]
 }
    '''

    '''#NOTE rezultat obtinut: "---> TEST-note: tabel 0 linii factura contine:...(nxt lines)..." #NOTE PASS OK for RENware invoice, only one line and data is OK
{
    'data': [
        ['', '', '', '', '', '', '', '', '', '', '', ''],
        ['', 1, '', '', '', 2, 3, '', 4, '5 = 3 x 4', '6 = 5 x 19%', ''],
        ['', 'Elaborare documentatie tehnica aplicatie NEXGEN.AI', '', '', '', 'buc', 1, '', 14807.4, 14807.4, 2813.41, '']
    ],
    'keycols': [
        '',
        'Denumirea produselor sau a serviciilor',
        '',
        '',
        '',
        'UM',
        'Cant.',
        '',
        'Pret unitar\n(fara TVA)\n- RON -',
        'Valoarea\n(fara TVA)\n- RON -',
        'TVA\n- RON -',
        ''
    ],
    'keyrows': [
        '',
        '0',
        1
    ]
 }
    '''


    #NOTE result is: (`invoice_header_area`, `invoice_lines_area`, `invoice_footer_area`)
    return (None, invoice_lines_area, None) #FIXME update with the other zones whene ready









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



