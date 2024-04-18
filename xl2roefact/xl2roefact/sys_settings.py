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
InvoiceTypes = [
    {
        "code": "normal",  # regular invoice (RO: factura normala) type (ie, not intra-community for example)
        "value": "380"
    },
    # ... more invoice types here in future (v > 0.6)
]


#--- 2. PARAMETERS section ---

# Enumeration used by CLI app for invoice typrs argument / option
class InvoiceTypesEnum(str, Enum):
    _k = _v = None
    for inv_type in InvoiceTypes:
        nonlocal _k, _v  # prevent errors when `_k` is an existing key as becoming global variable by applying `local()`
        for _k, _v in inv_type.items():
            locals()[_k] = _v
            



#--- 99. TEST section ---
print("**** InvoiceTypesEnum definition:")  #FIXME dbg can drop
pprint(InvoiceTypesEnum)  #FIXME dbg can drop
print("**** ---- End of InvoiceTypesEnum definition")  #FIXME dbg can drop



