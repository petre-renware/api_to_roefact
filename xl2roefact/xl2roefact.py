#!./.wenv_xl2roefact/bin/python3 #FIXME attn to this path if intend to move in modules/

""" xl2roefact - module to create a unified class for all xl2roefact and to be used as liibrary by any other external systems

Identification:
    code-name: `xl2roefact`
    copyright: (c) 2023 RENWare Software Systems
    author: Petre Iordanescu (petre.iordanescu@gmail.com)

"""

# general libraries
import os
# from pathlib import Path #NOTE see if keep / need it
from datetime import datetime
from colorama import Fore, Back, Style

# xl2roefact specific libraries
import rdinv as rdinv
import wrxml as wrxml
import chkxml as chkxml
import ldxml as ldxml
import chkisld as chkisld


class BaseProc():

    def __init__(self):
        """set directories environment: #NOTE CURRENT directory (as returned by OS `pwd` where from application is launched)
        """
        self.current_directory = None
        self.source_source_files_directoryectory = None
        self.invoice_worksheet = None
        #
        self.current_directory = os.getcwd()
        print(f"{Fore.YELLOW}DEBUG-note:{Style.RESET_ALL} class `BaseProc`, method `__init__, current directory is: {self.current_directory}") #NOTE for debug purposes
        # set directories environment: #NOTE MODULE file directory (where module is located as efective file)
        self.source_source_files_directoryectory = os.path.split(__file__)[0] # in all cases returns a list with 2 elements, path and file
        print(f"{Fore.YELLOW}DEBUG-note:{Style.RESET_ALL} class `BaseProc`, method `__init__, module directory is: {self.source_source_files_directoryectory}") #NOTE for debug purposes


    def get_directories(self):
        """simple utility method to get outside this class what directories was detected (and will be used)
        """
        return self.current_directory, self.source_source_files_directoryectory


    def set_invoice_to(self, invoice_to_process):
        """set current "to process" invoice (act as delayed initialize instead of sending at __init__)
        """
        self.crt_xl_file_to_process = invoice_to_process
        return


    def set_invoice_worksheet_to(self, invoice_worksheet):
        """set invoice worksheet name
        """
        self.invoice_worksheet = invoice_worksheet


    def read_invoice(self):
        """implement module `RDINV`
        """
        # print(f"{Fore.YELLOW}DEBUG-note:{Style.RESET_ALL} class `BaseProc`, method `read_invoice`, excel file to process: {self.crt_xl_file_to_process}") #NOTE for debug purposes
        _ = rdinv.rdinv(self.crt_xl_file_to_process, self.invoice_worksheet) #TODO return should be used but for now (test phase) is ok #FIXME - ...hereuare...wip... !!!






#
# #TODO_@final: this section is intended to be used for EXE CLI application
if __name__ == "__main__":
    print(f"\n*** Module {Fore.RED} xl2roefact {Style.RESET_ALL} launched on {Fore.GREEN}{datetime.now()}{Style.RESET_ALL}")

    _invoice_processor = BaseProc()
    _crt_directory, _source_files_directory = _invoice_processor.get_directories() #TODO subject of CONFIG
    _excel_files_directory = "excel_invoices/" #TODO subject of CONFIG


    #FIXME for test --- RENware invoice
    invvoice_to_process = "fact_RENF1004.xlsx"
    _invoice_processor.set_invoice_to(os.path.join(_crt_directory, _excel_files_directory, invvoice_to_process))
    # _invoice_processor.set_invoice_worksheet_to("FACTURA FINALA") #NOTE if not specified should open firts one...
    _invoice_processor.read_invoice()


    #FIXME another test --- Kraftanlagen invoice
    invvoice_to_process = "Fact _Petrom_11017969.xlsx" #NOTE original document name, next is my test for splitting
    _invoice_processor.set_invoice_to(os.path.join(_crt_directory, _excel_files_directory, invvoice_to_process))
    # _invoice_processor.set_invoice_worksheet_to("Factura(Invoice)") #NOTE if not specified should open firts one...
    _invoice_processor.read_invoice()



