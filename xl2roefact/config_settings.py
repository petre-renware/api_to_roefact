"""  Application configuration and setting parameters
    NOTE README me before making changes:
        - each parameter has a short help (lines starting with `#` character) - read it before changing that parameter
        - do not change parametrs name as specified before equal (`=`) sign
        - lists are enclosed in sqaured brackets (`[...]`) and items are separated by comma character (`,`)
        - strings are enclosed in `"` characters
        - if you want to clear a list (for example you do not wants any options inside) just let it as `<PARAMETR NAME> = []` - do not drop that parameter
        - do not add supplementary parameters, they will not be used without software changes (also risk to induce potential errors)

    Identification:
        code-name: `config_settings`
        copyright: (c) 2023 RENWare Software Systems
        author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

"""---------------------------------------------------------------------------------------------------------------------------
# NOTE: parametrii utilizati in de comanda: `xl2json`, functionalitate: extragere date Excel si export in JSON (modul `rdinv)
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

# --- contine secventele de caractere care permit inceputul zonei (sub-tabelului) ce contine liniile facturii
INVOICE_ITEMS_SUBTABLE_MARKER: list[str] = [" crt", "no. crt", "nr. crt", "#"]

# --- numarul facturii
# acest parametru permit identificarea numarului facturii, astfel sistemul va cauta dupa secventele din parametrul
# `INVOICE_NUMBER_IDENTIFICATION_LABELS`,... (cautarea fiind indiferenta de marimea caracterelor).
# Aceasta reprezentind "eticheta" unde se presupune a fi numarul facturii.  Pentru a gasi numarul efectiv al facturii,
# sistemul va cauta in directiile DREAPTA (UP) si apoi daca nu gaseste JOS (DOWN)
INVOICE_NUMBER_IDENTIFICATION_LABELS: list[str] = ["nr. fact", "nr fact", "numar fact", "fact nr", "factura num", "invoice number", "invoice no", "invoice:"]



