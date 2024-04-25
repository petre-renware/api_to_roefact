"""System database and parameters.

This module acts as an "ORM" between `xl2roefact` system and different data objects. It contains:

* tinny physical data objects (Section 1.)
* logical data objects (Section 2.)
* interfaces to external data objects as files or other specialized systems (Section 2.)

Notes:

* "Sections 1, sl , ..." organization of code even is just a pure visual one, is recommended to be respected and followed it being intended to increase code readability and latter maintainability.
* IMPORTANT to keep in mind: This module IS NOT intended to be modified by end users or administrators. Only development stuff can alter this database because application code must be updated accordingly.
* for updaters remark: because dependencies, code sections should follow strict enumerated order in comments

References:

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


"""Section 1. DATABASE in-module physical store
"""

# Object that keep allowed InvoiceType codes:
# - `key`: displayed type to choose
# - `value`: value used for JSON-`cbc_InvoiceTypeCode` key respectively XML-`cbc:InvoiceTypeCode` attribute
# WARNING: object records hardly impact invoice VAT calculation and recognition
InvoiceTypes = dict(
    NORMALA = "380",  # regular invoice (RO: factura normala) type (ie, not intra-community for example)
    # ... more invoice types here in future (v > 0.6)
)




"""Section 2. INTERFACES & LOGICAL data
"""

# Enumeration used by CLI app for invoice typrs argument / option
InvoiceTypesEnum = Enum("InvoiceTypesEnum", InvoiceTypes)



