#!./.wenv_base_proc/bin/python3 #FIXME attn to this path if intend to move in modules/

""" BASE_PROC - module to create a unified class for all BASE_PROC and to be used as liibrary by any other external systems

Identification:
    code-name: `base_proc`
    copyright: (c) 2023 RENWare Software Systems
    author: Petre Iordanescu (petre.iordanescu@gmail.com)

"""

# general libraries
import os
# from pathlib import Path #NOTE see if keep / need it
from datetime import datetime
from colorama import Fore, Back, Style

# BASE_PROC specific libraries
import modules.rdinv as rdinv
import modules.wrxml as wrxml
import modules.chkxml as chkxml
import modules.ldxml as ldxml
import modules.chkisld as chkisld


#TODO CLASS_TRANSFORM_FUTURE_ACTIONS: this should be transformed in a class (including specific imports)
class BaseProc():

    #TODO CLASS_TRANSFORM_FUTURE_ACTIONS: __init()__ method
    def __init__(self):
        """set directories environment: #NOTE CURRENT directory (as returned by OS `pwd` where from application is launched)
        """
        self.current_directory = os.getcwd()
        print(f"DEBUG-note: class `BaseProc`, method `__init__, current directory is: {self.current_directory}") #NOTE for debug purposes
        # set directories environment: #NOTE MODULE file directory (where module is located as efective file)
        self.module_directory = os.path.split(__file__)[0] # in all cases returns a list with 2 elements, path and file
        print(f"DEBUG-note: class `BaseProc`, method `__init__, module directory is: {self.module_directory}") #NOTE for debug purposes


    def get_directories(self):
        """simple utility method to get outside this class what directories was detected (and will be used)
        """
        return self.current_directory, self.module_directory


    def set_invoice_to(self, invoice_to_process):
        """set current "to process" invoice (act as delayed initialize instead of sending at __init__)
        """
        self.crt_xl_file_to_process = invoice_to_process
        return


    def set_invoice_worksheet_to(self, invoice_worksheet):
        """set invoice worksheet name
        """
        self.invoice_worksheet = invoice_worksheet


    #TODO CLASS_TRANSFORM_FUTURE_ACTIONS: read_invoice() method
    def read_invoice(self):
        """implement module `RDINV`
        """
        # print(f"DEBUG-note: class `BaseProc`, method `read_invoice`, excel file to process: {self.crt_xl_file_to_process}") #NOTE for debug purposes
        _ = rdinv.rdinv(self.crt_xl_file_to_process, self.invoice_worksheet) #TODO return should be used but for now (test phase) is ok #FIXME - ...hereuare...wip... !!!







# here start the main job of this module


print(f"\n*** Module {Fore.RED} BASE_PROC {Style.RESET_ALL} launched on {Fore.GREEN} {datetime.now()} {Style.RESET_ALL}")

_unknown_udefined_yet_name = BaseProc() #FIXME set an usefull variable name here
_crt_dir, _mdl_dir = _unknown_udefined_yet_name.get_directories()


#FIXME for test --- RENware invoice
tmp = "fact_RENF1004.xlsx"
tmp = os.path.join(_crt_dir, "test_data_and_specs/test_fact_RENware/", tmp)
#---------------------------------------
_unknown_udefined_yet_name.set_invoice_to(tmp)
_unknown_udefined_yet_name.set_invoice_worksheet_to("FACTURA FINALA")
_unknown_udefined_yet_name.read_invoice()
#FIXME ------------------------------------------------------------- end test area :: SHOULD DISPLAY "Cota TVA: 19%" #NOTE OK-PASS



#FIXME another test --- Kraftanlagen invoice
tmp = "Fact _Petrom_11017969.xlsx"
tmp = os.path.join(_crt_dir, "test_data_and_specs/test_fact_client/", tmp)
#---------------------------------------
_unknown_udefined_yet_name.set_invoice_to(tmp)
_unknown_udefined_yet_name.set_invoice_worksheet_to("Factura(Invoice)")
_unknown_udefined_yet_name.read_invoice()
#FIXME ------------------------------------------------------------- end test area :: SHOULD DISPLAY "Bucuresti / Sector 1 PETROM CITY" #NOTE OK-PASS

#FIXME PROBLEM HERE: xls binary format is not supported


