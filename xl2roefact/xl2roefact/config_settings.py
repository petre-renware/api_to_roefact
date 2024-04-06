"""Configuration and setting parameters.

Regulile recomandate se gasessc in documentul (recommended rules are in document) [`data/README_app_config_rules.md`](./data/README_app_config_rules.md)

    Public objects:

        `rules_content`: contains the rules text (rendered)

* copyright: (c) 2023 RENWare Software Systems
* author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

from pathlib import Path
import os
import sys
from rich.markdown import Markdown
import yaml
from pprint import pprint
from .libutils import hier_get_data_file

"""---------------------------------------------------------------------------------------------------------------------------
# NOTE: urmatorii parametri sunt utilizati pentru a obtine valori implicite (default) atunci cind nu sunt gasite anumite date / informatii.
#   Uzual ei sunt folositi de comanda `xl2json` reprezentind functionalitatea de extragere a datelor din Excel si exportul lor in formatul JSON (modulul `rdinv)
---------------------------------------------------------------------------------------------------------------------------"""

# --- coeficientul TVA implicit
# este utilizat de catre aplicatie in toate conditiile in care nu este gasit unul in fiserul de intrare
DEFAULT_VAT_PERCENT: float = 0.19

# --- denumirea unui produs ce nu poate fi identificat
# este utilizat de catre aplicatie in toate conditiile in care denumirea unui produs sau serviciu (liniile facturii) nu este specifcata
# denumirea este considerta necunoscuta atunci cind este lasata 'blank' sau pur si simplu celula respectiva este goala
DEFAULT_UNKNOWN_ITEM_NAME: str = "--- n/a ---"

# --- unitatea de masura implicita
# este utilizat de catre aplicatie in toate conditiile in care unitatea de masura unui produs sau serviciu (liniile facturii) nu este cunoscuta
# unitatea de masura este considerta necunoscuta atunci cind este lasata 'blank' sau pur si simplu celula respectiva este goala
DEFAULT_UNKNOWN_UOM: str|None = None

# --- moneda implicita
# este utilizat de catre aplicatie in toate conditiile in care pe factura nu este specifcata in clar o moneda
# specifcarea monedei ca sau in titlurile coloanelor nu este luata in considerare (nu este garantat ca este moneda reala a facturii !)
DEFAULT_CURRENCY: str = "RON"

# --- tara implicita
# aceste constante sunt utilizate ca si tara implicita pentru "parterii" facturilor in condtiile in care tarile "parterilor" nu sunt gasite
# in mod explicit pe factura (in zona de adresa). Prin sintagma "partener" pe factura sa intelege oricare din cele doua parti implicate in
# procesul de facturare, si anume: FURNIZORUL si CLIENTUL
DEFAULT_CUSTOMER_COUNTRY: str = "RO"
# ...and the corresponding one for supplier
DEFAULT_SUPPLIER_COUNTRY: str = "RO"


"""---------------------------------------------------------------------------------------------------------------------------
# NOTE: "pattern-uri" (sabloane) de identificare si regasire a datelor folositi de
#   comanda `xl2json` reprezentind functionalitatea de extragere a datelor din Excel si exportul lor in formatul JSON (modulul `rdinv)
---------------------------------------------------------------------------------------------------------------------------"""

# --- contine secventele de caractere care permit inceputul zonei (sub-tabelului) ce contine liniile facturii
PATTERN_FOR_INVOICE_ITEMS_SUBTABLE_MARKER: list[str] = [
    " crt", " crt.",
    "no. crt.", "no crt", "no. crt", "no crt.",
    "nr. crt.", "nr crt", "nr. crt", "nr crt.",
    "#",
]

# --- numarul facturii
# acest parametru permit identificarea numarului facturii, astfel sistemul va cauta dupa secventele din parametrul
# `PATTERN_FOR_INVOICE_NUMBER_LABEL`,... (cautarea fiind indiferenta de marimea caracterelor).
# Aceasta reprezentind "eticheta" unde se presupune a fi numarul facturii.  Pentru a gasi numarul efectiv al facturii,
# sistemul va cauta in directiile DREAPTA (UP) si apoi daca nu gaseste JOS (DOWN)
PATTERN_FOR_INVOICE_NUMBER_LABEL: list[str] = [
    "nr. fact", "nr fact", "numar fact", "fact nr", "factura num",
    "invoice number", "invoice no", "invoice:",
]

# --- moneda facturii
# pattern utilizat pentru a gasi moneda facturii (daca a fost specificata iar daca nu gaseste se va utiliza DEFAULT_CURRENCY)
PATTERN_FOR_INVOICE_CURRENCY_LABEL: list[str] = [
    "mone",
    "curr", "ccy"
]

# --- data facturii
# pattern utilizat pentru a gasi data facturii
# NOTE-1 in XML formatul utilizat este YYYY-MM-DD
# NOTE-2 in celula Excel aferenta datei se asteapta ca formatul sa fie cel stadard de data calendaristica (ATENTIE: NU string)
PATTERN_FOR_INVOICE_ISSUE_DATE_LABEL: list[str] = [
    "data", "data fact", "data emit",
    "date", "invoice date", "issue date",
]

# --- client (customer)
# pattern utilizat pentru a gasi aria (zona) cu datele furnizorului
PATTERN_FOR_INVOICE_CUSTOMER_SUBTABLE_MARKER: list[str] = [
    "clien",
    "custo",
    "sc", "s.c", "diviz", "depart",
    "sa", "s.a",
    "srl", "s.r.l",
    "pfa", "p.f.a",
    "ra", "r.a",
]

# --- numele legal al companiei
# pattern utilizat pentru regasirea numelui legal al clientului
# NOTE se presupune a fi la inceputul zonei cu datele clientului, deci se ca cauta dupa acelasi pattern
PATTERN_FOR_CUSTOMER_LEGAL_NAME = PATTERN_FOR_INVOICE_CUSTOMER_SUBTABLE_MARKER

# --- pattern pentru regasirea codului unic de inregistrare (sau Company ID in engleza) (pattern comun pentru client si furnizor)
PATTERN_FOR_PARTNER_ID = [
    "cui", "c.u.i",
    "cif", "c.i.f",
    "id",
]

# --- pattern pentru regasirea nr de inreg la Registrul Comertului
PATTERN_FOR_PARTNER_REGCOM = [
    "reg com", "reg. com", "comert",
]

# --- pattern-uri pentru regasirea bancii si a contului bancar
PATTERN_FOR_PARTNER_BANK = [
    "banc", "bank",
]
PATTERN_FOR_PARTNER_IBAN = [
    "iban", "cont", "bank acc",
]

# --- pattern pentru regasirea datelor de contact (tel, email)
PATTERN_FOR_PARTNER_TEL = [
    "tel", "phon",
]
PATTERN_FOR_PARTNER_EMAIL = [
    "mail", "email", "e-mail",
]

# --- pattern pentru regasirea adresei (pattern comun pentru client si furnizor)
# este important ca ordinea de cautare sa permita ca sansele sa fie maximizate pentru cautarea adresei complete sau macar a tarii
PATTERN_FOR_PARTNER_ADDRESS = [
    "adr", "addr",
    "tara", "count",
    "locali", "oras",
    "city", "town",
    "str",
]
PATTERN_FOR_PARTNER_ADDRESS_COUNTRY = [
    "tara", "countr",
]
PATTERN_FOR_PARTNER_ADDRESS_CITY = [
    "judet", "county",
    "locali",
    "oras", "city", "town", "land"
]
PATTERN_FOR_PARTNER_ADDRESS_STREET = [
    "str", "sos", "bd", "calea",
    "ave", "highwa",
]
PATTERN_FOR_PARTNER_ADDRESS_ZIPCODE = [
    "cod pos", "zip cod", "postal",
]

# --- furnizor (supplier)
# pattern utilizat pentru a gasi aria (zona) cu datele furnizorului
PATTERN_FOR_INVOICE_SUPPLIER_SUBTABLE_MARKER: list[str] = [
    "furniz", "proprie",
    "suppl", "owne",
    "sc", "s.c", "diviz", "depart",
    "sa", "s.a",
    "srl", "s.r.l",
    "pfa", "p.f.a",
    "ra", "r.a",
]

# --- numele legal al companiei furnizoare
# pattern utilizat pentru regasirea numelui legal al furnizorului
# NOTE se presupune a fi la inceputul zonei cu datele furnizorului, deci se ca cauta dupa acelasi pattern
PATTERN_FOR_SUPPLIER_LEGAL_NAME = PATTERN_FOR_INVOICE_SUPPLIER_SUBTABLE_MARKER




# ------- NOTE: the following code runs unconditionally at module import

# section to read settings from external data file
file_to_use = hier_get_data_file("app_settings.yml")
python_object = None  # suppose no settings loaded
if file_to_use:
    yaml_in = file_to_use.read_text()
    python_object = yaml.safe_load(yaml_in)
    print("***INFO: Application settings loaded from file.")
# assign `python_object` to locals() environment...
if python_object is not None:  # ...only if previous method has read something
    locals().update(python_object)
else:  # if nothing or wrong read from previous method, settings applied will remain to values hard-coded in this module
    print("***INFO: Application settings loaded from application code (default settings).")




