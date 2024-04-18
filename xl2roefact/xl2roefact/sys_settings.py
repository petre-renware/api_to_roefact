"""System database and parameters.

This module IS NOT intended to be modified by end users or administrators.
Only development stuff can alter this database because application code must be updated accordingly.

* NOTE for updaters: because dependencies code sections should follow the strict order they was enumerated 

* copyright: (c) 2024 RENWare Software Systems
* author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

from pathlib import Path
import os
import sys
from rich.markdown import Markdown
import yaml
from pprint import pprint
from .libutils import hier_get_data_file
from enum import Enum


#--- 1. DATABASE section ----

# Object that keep allowed InvoiceType codes (derived as `cbc_InvoiceTypeCode`)
#  WARNING: object records hardly impact invoice VAT calculation and recognition
InvoiceType = {
    "description": "Factura normala",  # regular invoice type (ie, not intra-community for example) 
    "code": "normal", 
    "value": "380"
}


#--- 2. PARAMETERS section ---

# Enumeration used 
class InvoiceTypesEnum(str, Enum):
    eval{InvoiceType["code"]) = InvoiceType["value"]
    




