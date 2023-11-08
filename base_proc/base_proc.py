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


if __name__ == "__main__": #NOTE for debug purposes - used only when directly launched (not from a wrapper or other sysetem)
    print(f"\n*** Module {Fore.RED} BASE_PROC {Style.RESET_ALL} launched on {Fore.GREEN} {datetime.now()} {Style.RESET_ALL}")


#TODO CLASS_TRANSFORM_FUTURE_ACTIONS: this should be transformed in a class (including specific imports)
#class BaseProc():

# BASE_PROC specific libraries
import modules.rdinv as rdinv
import modules.wrxml as wrxml
import modules.chkxml as chkxml
import modules.ldxml as ldxml
import modules.chkisld as chkisld


#TODO CLASS_TRANSFORM_FUTURE_ACTIONS: __init()__ method
# set directories environment: #NOTE CURRENT directory (as returned by OS `pwd` where from application is launched)
current_directory = os.getcwd()
print(f"DEBUG-note: current directory is: {current_directory}") #NOTE for debug purposes
# set directories environment: #NOTE MODULE file directory (where module is located as efective file)
module_directory = os.path.split(__file__)[0] # in all cases returns a list with 2 elements, path and file
print(f"DEBUG-note: module directory is: {module_directory}") #NOTE for debug purposes


#TODO CLASS_TRANSFORM_FUTURE_ACTIONS: raad_invoice() method
tmp = "fact_RENF1004.xlsx"
crt_xl_file_to_process = os.path.join(current_directory, "test_data_and_specs/test_fact_RENware/", tmp)
print(f"DEBUG-note: excel file to process: {crt_xl_file_to_process}") #NOTE for debug purposes
_ = rdinv.rdinv(crt_xl_file_to_process) #TODO return should be used but for now (test phase) is ok #FIXME - ...hereuare...wip... !!!









