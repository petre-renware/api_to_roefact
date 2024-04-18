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

# Object that keep allowed InvoiceType codes:
# - `key`: displayed type to choose
# - `value`: value used for JSON-`cbc_InvoiceTypeCode` key respectively XML-`cbc:InvoiceTypeCode` attribute
# WARNING: object records hardly impact invoice VAT calculation and recognition
InvoiceTypes = {
    "NORMALA": "380",  # regular invoice (RO: factura normala) type (ie, not intra-community for example)
    "TEST": "tst",  #FIXME dbg drop me. Sample record for test
    # ... more invoice types here in future (v > 0.6)
}



#--- 2. PARAMETERS section ---

# Enumeration used by CLI app for invoice typrs argument / option
class InvoiceTypesEnum(str, Enum):
    for _k, _v in InvoiceTypes.items():
        local()[_k] = _v


#--- 99. TEST section ---
print(f"\n**** Object resulted {list(InvoiceTypesEnum)}")  #FIXME dbg drop

