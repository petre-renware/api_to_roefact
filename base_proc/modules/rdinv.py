#!../.wenv_base_proc/bin/python3

import pylightxl as xl
from datetime import datetime
from colorama import Fore, Back, Style

def rdinv(file_to_process: str):
    """ RDINV - modul de procesare a fisierului format XLSX ce contine factura si colectare a datelor aferente

    Identification:
        code-name: `rdinv`
        copyright: (c) 2023 RENWare Software Systems
        author: Petre Iordanescu (petre.iordanescu@gmail.com)

    Specifications:
        document: `110-SRE-api_to_roefact_requirements.md` section `Componenta BASE_PROC`
        INTRARI: fisier format XLSX ce contine factura emisa (cod: `f-XLSX`)
        IESIRI: fisier format JSON imagine a datelor facturii (cod: `f-JSON`)
    """

    import pylightxl as xl

    print(f"*** Module `rdinv` started at {Fore.GREEN} {datetime.now()} {Style.RESET_ALL} to process file {Fore.GREEN} {file_to_process} {Style.RESET_ALL}")

    ... #TODO my code here
    return None


