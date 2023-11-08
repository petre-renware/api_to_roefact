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



    #FIXME for test read cell B13 which should contain text "Cota TVA: 19%"
    tmp = ws.address(address="B13")
    print(f"---> TEST-note: cell read contains: {tmp}")
    #FIXME -------------------------------------------------------------------------------------- END OF TEST here {#NOTEOK-PASSED}

    ... #TODO ...hereuare...

    return True


