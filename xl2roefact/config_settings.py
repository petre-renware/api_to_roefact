"""  Application configuration and setting parameters
    NOTE README me before making changes:
        - each parameter has a short help (lines starting with `#` character) - read it before changing that parameter
        - do not change parametrs name as specified before equal (`=`) sign
        - lists are enclosed in sqaured brackets (`[...]`) and items are separated by comma character (`,`)
        - strings are enclosed in `"` characters
        - if you want to clear a list (for example you do not wants any options inside) just let it as `<PARAMETR NAME> = []` - do not drop that parameter
        - do not add supplementary parameters, they will not be used without software changes (also risk to induce potential errors)

    Identification:
        code-name: `rdinv`
        copyright: (c) 2023 RENWare Software Systems
        author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

# coeficientul TVA implicit
#   este utilizat de catre aplicatie in toate conditiile in care nu este gasit unul in fiserul de intrare
DEFAULT_VAT_PERCENT = 0.19


# denumirea unui produs ce nu poate fi identificat
#   este utilizat de catre aplicatie in toate conditiile in care denumirea unui produs sau serviciu (liniile facturii) nu este specifcata
#   denumirea este considerta necunoscuta atunci cind este lasata 'blank' sau pur si simplu celula respectiva este goala
DEFAULT_UNKNOWN_ITEM_NAME = "--- n/a ---"


# unitatea de masura implicita
#   este utilizat de catre aplicatie in toate conditiile in care unitatea de masura unui produs sau serviciu (liniile facturii) nu este cunoscuta
#   unitatea de masura este considerta necunoscuta atunci cind este lasata 'blank' sau pur si simplu celula respectiva este goala
DEFAULT_UNKNOWN_UOM = None


# moneda implicita
#   este utilizat de catre aplicatie in toate conditiile in care pe factura nu este specifcata in clar o moneda
#   specifcarea monedei ca sau in titlurile coloanelor nu este luata in considerare (nu este garantat ca este moneda reala a facturii !)
DEFAULT_CURRENCY = "RON"



# contine secventele de caractere care permit inceputul zonei (sub-tabelului) ce contine liniile facturii
INVOICE_ITEMS_SUBTABLE_MARKER = [" crt", "no. crt", "nr. crt", "#"]



