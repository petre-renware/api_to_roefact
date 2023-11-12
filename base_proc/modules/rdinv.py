#!../.wenv_base_proc/bin/python3
"""  RDINV - modul de procesare a fisierului format XLSX ce contine factura si colectare a datelor aferente

    Identification:
        code-name: `rdinv`
        copyright: (c) 2023 RENWare Software Systems
        author: Petre Iordanescu (petre.iordanescu@gmail.com)

    Specifications:
        document: `110-SRE-api_to_roefact_requirements.md` section `Componenta BASE_PROC`
        INTRARI: fisier format XLSX ce contine factura emisa (cod: `f-XLSX`)
        IESIRI: fisier format JSON imagine a datelor facturii (cod: `f-JSON`)
"""

# general modules (should be already imported by BaseProc class)
from datetime import datetime
from colorama import Fore, Back, Style
import copy

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

    ''' #NOTE quick plan:
    - [ ] identifiy invoice table with its lines (products, services, ..., items) - start of table (as known KEYROWS/KEYCOLS) should be things like:
        - "No. crt." in Kraftlangen invoice, "Nr. crt" in RENware invoice
        - generally **containig "crt" string** or "#" string as single or delimited LR with spaces

    - [ ] then isolate header and footer
            ==> set variable for these zones: `invoice_header_area`, `invoice_lines_area`, `invoice_footer_area`
    '''

    # string-markers to search for to isolate `invoice_lines_area` #TODO to be unified (how? - search the cell containg text fragments --> get text from that cell --> use it as `ssd()` parameter)
    # #NOTE_ATT_README: tmp_items_table_marker_string = "crt" #FIXME drop me - DOES NOT WORK, search is exact... TRY THIS as "unified string"
    tmp_items_table_marker_string = "No. crt." #NOTE Kraftlangen invoice
    #tmp_items_table_marker_string = "Nr. crt" #NOTE RENware invoice

    # detect all cells that should be changed to SYS_FILLED_EMPTY_CELL
    detected_cells_which_will_be_fake_filled = _get_merged_cells_tobe_changed(file_to_process, invoice_worksheet_name) # ...hereuare...
    #print(f"----------DETECTED RANGES: {detected_cells_which_will_be_fake_filled}") #FIXME drop me as debugging

    # scan all detectected cell and change them
    for _cell_index in detected_cells_which_will_be_fake_filled:
        _cell_row = _cell_index[0]
        _cell_col = _cell_index[1]
        #print(f"to update cell {_cell_index} @ row={_cell_row} col={_cell_col}") #FIXME drop after test
        ws.update_index(row = _cell_row, col = _cell_col, val = SYS_FILLED_EMPTY_CELL)
        #print(f"cell {_cell_index} updated. new read va is: {ws.index(row = _cell_row, col = _cell_col)}") #FIXME drop after test
    '''#NOTE: RESULTS obtained for Kraftlangen invoice:
---> TEST-note: tabel 0 linii factura contine:
{   'keyrows': ['___sys_filled_empty_cell', 1],
    'keycols': ['Denumirea lucrarii                                  (Request description)', '___sys_filled_empty_cell', 'Cantitatea (Quantity)', 'Pret unitar (Unit price)', 'Cota TVA (VAT %)', 'Valoare fara TVA (Value without VAT)', 'Valoare TVA (Value VAT)'],
    'data': [['___sys_filled_empty_cell', '___sys_filled_empty_cell', '___sys_filled_empty_cell', '___sys_filled_empty_cell', '___sys_filled_empty_cell', '___sys_filled_empty_cell', '___sys_filled_empty_cell'], ['Inlocuit conducta PSI coloana C2 DAV.', '___sys_filled_empty_cell', 1, 42756.08, 0.19, 42756.08, 8123.6552]]
}

---> TEST-note: keyword KEYROWS contine: ['___sys_filled_empty_cell', 1]
---> TEST-note: keyword KEYCOLS contine: ['Denumirea lucrarii                                  (Request description)', '___sys_filled_empty_cell', 'Cantitatea (Quantity)', 'Pret unitar (Unit price)', 'Cota TVA (VAT %)', 'Valoare fara TVA (Value without VAT)', 'Valoare TVA (Value VAT)']
---> TEST-note: keyword DATA contine: [['___sys_filled_empty_cell', '___sys_filled_empty_cell', '___sys_filled_empty_cell', '___sys_filled_empty_cell', '___sys_filled_empty_cell', '___sys_filled_empty_cell', '___sys_filled_empty_cell'], ['Inlocuit conducta PSI coloana C2 DAV.', '___sys_filled_empty_cell', 1, 42756.08, 0.19, 42756.08, 8123.6552]]
    ''' #TODO ...hereuare... to analyze & clean
    print("-------------------------GATA TEST") #FIXME drop me && DO NOT FORGET @ FINAL OF PROCESS to "re-empty" all cells containing SYS_FILLED_EMPTY_CELL - that's because you'll need original xl file to write a new sheet with returne ANAF receipt number & text


    invoice_lines_area = ws.ssd(keycols = tmp_items_table_marker_string, keyrows = tmp_items_table_marker_string)
    if (invoice_lines_area is None or ((isinstance(invoice_lines_area, list)) and len(invoice_lines_area) < 1)): # there was not detected any area candidate to "invoice items / lines", so will exit rasing error
        print(f"{Fore.RED}***FATAL ERROR - Cannot find any candidate to for invoice ITEMS. Worksheet - ({invoice_data_worksheet}) in Module {Fore.RED} RDINV (code-name: `rdinv`). File processing terminated{Style.RESET_ALL}")
        return False
    #FIXME test if list has more items, because will contain ALL DETECTECTED AREAS, so retain only first one [0]
    if isinstance(invoice_lines_area, list) and len(invoice_lines_area) > 0:
        invoice_lines_area = invoice_lines_area[0] #FIXME next code suppose that retain only first one [0]
    #
    # get the 3 sections (keywords) of `invoice_lines_area` dictionary: "keyrows", "keycols" and "data"
    invoice_lines_area_keyrows = invoice_lines_area["keyrows"]
    invoice_lines_area_keycols = invoice_lines_area["keycols"]
    invoice_lines_area_data = invoice_lines_area["data"]


    #FIXME --------------------------------------- TEST area
    print(f"{Fore.YELLOW}")
    print(f"---> TEST-note: tabel 0 linii factura contine:") #NOTE test should be an array of arrays (matrix) with invoice items
    print(invoice_lines_area)
    print()
    print(f"---> TEST-note: keyword KEYROWS contine: {invoice_lines_area_keyrows}")
    print(f"---> TEST-note: keyword KEYCOLS contine: {invoice_lines_area_keycols}")
    print(f"---> TEST-note: keyword DATA contine: {invoice_lines_area_data}")
    print()
    ''' rezultat obtinut
    KEYROWS: `[]`
    KEYCOLS: `['Denumirea lucrarii                                  (Request description)']`
    DATA: `[]`
    '''
    print(f"{Style.RESET_ALL}")
    #FIXME --------------------------------------- TEST area



    #FIXME for test read cell B13 which should contain text "Cota TVA: 19%"
    #tmp = ws.address(address="B13")
    #print(f"---> TEST-note: cell read contains: {tmp}")
    #FIXME -------------------------------------------------------------------------------------- END OF TEST here {#NOTE OK-PASSED}

    ... #TODO ...hereuare...

    return True #TODO here should return an usful result such a list with invoice identified areas...






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



