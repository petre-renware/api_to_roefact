"""System database with parameters.

This module IS NOT intended to be modified by end users or administrators. Only development stuff can alter this database because application code must be updated accordingly.

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


# Object that keep allowed InvoiceType codes (derived as `cbc_InvoiceTypeCode`) 
InvoiceType = {
    "name": "Factura normala",
    "code": "380"
}



