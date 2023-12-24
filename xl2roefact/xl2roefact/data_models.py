#!../.venv/bin/python3
"""  INVOICE JSON STRUCTURE - the JSON format of invoice

    Identification:
        code-name: `invoice_json_structure`
        copyright: (c) 2023 RENWare Software Systems
        author: Petre Iordanescu (petre.iordanescu@gmail.com)

    Specifications:
        document: usual invoice columns, respecting as possible the following XSD schemes
        ```
        xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
        xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
        xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
        xmlns:ns4="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2 http://docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd">
        ```
"""

import os
from datetime import datetime, timezone, tzinfo
from rich import print
from typing import TypedDict  #NOTE: doc helper `https://mypy.readthedocs.io/en/stable/typed_dict.html`
import copy
from pprint import pprint
from string import ascii_lowercase
import json
from libutils import isnumber, find_str_in_list # local library



#NOTE: *** TypedDict *** doc helper `https://mypy.readthedocs.io/en/stable/typed_dict.html`



""" #FIXME invoice model:
- first level:
    - invoice header data: owner, customer, invoice number/id, issued data
    - invice item lines (see #NOTE-IIL)
    - invoice footer data: delivery data, delivered on date ..., emis de... ??? (see RO-EFact XML to see what data require ANAF)
- #NOTE-IIL: invoice item lines structure (just orienrarive - get real from `rdinv.py`):
    ```
    _line_info = {
        "cac:InvoiceLine": {
            "cbc:ID": str,
            "cbc:InvoicedQuantity": float,
            "cbc:unitCode": str,
            "cac:Item": {
                "cbc:Name": str,
                "cac:ClassifiedTaxCategory": {
                    "cbc:Percent": float,
                    "cac:TaxScheme": {
                        "cbc:ID": "VAT"str
                    } if _item_quantity else None
                }
            },
            "cac:Price": {
                "cbc:PriceAmount" : float,
                "cbc:currencyID": str
            },
            "cbc:LineExtensionAmount": float
        }
    }
    ```
"""


""" #FIXME owner & customer models:
- classic attributes: name, CUI-ID-RegNo, legal_RegCom-Jnn/yyy... number, bank account, address, ...
"""




