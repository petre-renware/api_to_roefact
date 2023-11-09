#!../.wenv_base_proc/bin/python3




def rdinv(file_to_process: str, invoice_data_worksheet: str = None):
    """ RDINV - modul de procesare a fisierului format XLSX ce contine factura si colectare a datelor aferente

    Identification:
        code-name: `rdinv`
        copyright: (c) 2023 RENWare Software Systems
        author: Petre Iordanescu (petre.iordanescu@gmail.com)

    Specifications:
        document: `110-SRE-api_to_roefact_requirements.md` section `Componenta BASE_PROC`
        INTRARI: fisier format XLSX ce contine factura emisa (cod: `f-XLSX`)
        IESIRI: fisier format JSON imagine a datelor facturii (cod: `f-JSON`)

    Arguments:
        file_to_process: the invoice file (exact file with path)
        invoice_data_worksheet: the worksheet containing invoice

    Important variables:
        db: htxl object with invoice EXCEL (as a whole)
        ws: pylightxl object with invoice WORKSHEET
    """
    # general modules (should be already imported by BaseProc class)
    from datetime import datetime
    from colorama import Fore, Back, Style

    import pylightxl as xl

    print(f"\n*** Module {Fore.RED} RDINV (code-name: `rdinv`){Style.RESET_ALL} started at {Fore.GREEN}{datetime.now()} {Style.RESET_ALL} to process file {Fore.GREEN} {file_to_process} {Style.RESET_ALL}")

    # read Excel file with Invoice data
    try:
        db = xl.readxl(fn=file_to_process)
    except:
        print(f"{Fore.RED}***FATAL ERROR - Cannot open Excel file {file_to_process} (possible problems: file corruted, wrong type only XLSX accetpted, file does not exists or was deleted, operating system vilotation) in Module {Fore.RED} RDINV (code-name: `rdinv`) {Style.RESET_ALL}. Process terminated {Style.RESET_ALL}")
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
        print(f"{Fore.RED}***FATAL ERROR - Cannot open Excel specified Worksheet ({invoice_data_worksheet}) in Module {Fore.RED} RDINV (code-name: `rdinv`) {Style.RESET_ALL}. Process terminated {Style.RESET_ALL}")
        return False
    #print(f"{Fore.YELLOW}DEBUG-note:{Style.RESET_ALL} `rdinv` module, Excel worksheet read (`ws` variable) as: {ws} {Style.RESET_ALL}") #NOTE for debug purposes


    ''' #NOTE quick plan:
    - identifiy invoice table with its lines (products, services, ..., items)
        - start of table (as known KEYROWS/KEYCOLS) should be things like:
            - "No. crt." in Kraftlangen invoice, "Nr. crt" in RENware invoice
            - generally **containig "crt" string** or "#" string as single or delimited LR with spaces

    - EXAMPLE IS: `ssd = db.ws('Sheet1').ssd(keycols="KEYCOLS", keyrows="KEYROWS")` ... where start line & col really contain text KEYCOLS, KEYROWS

    - then isolate header and footer
            ==> set variable for these zones: `invoice_header_area`, `invoice_lines_area`, `invoice_footer_area`
    '''
    tmp_items_table_marker_string = "No. crt." #NOTE Kraftlangen invoice
    #tmp_items_table_marker_string = "Nr. crt" #NOTE RENware invoice
    invoice_lines_area = ws.ssd(keycols = tmp_items_table_marker_string, keyrows = tmp_items_table_marker_string)
    #FIXME test if list because will contain ALL DETECTECTED AREAS, so retain only first one [0]
    #FIXME if not list then kkep it as is...



    print(f"---> TEST-note: tabel 0 linii factura contine: {invoice_lines_area}") #FIXME test should be an array of arrays (matrix) with invoice items
    ''' rezultat obtinut
    [{'keyrows': [], 'keycols': ['Denumirea lucrarii                                  (Request description)'], 'data': []}]
    '''




    #FIXME for test read cell B13 which should contain text "Cota TVA: 19%"
    #tmp = ws.address(address="B13")
    #print(f"---> TEST-note: cell read contains: {tmp}")
    #FIXME -------------------------------------------------------------------------------------- END OF TEST here {#NOTE OK-PASSED}

    ... #TODO ...hereuare...

    return True #TODO here should return an usful result such a list with invoice identified areas...


