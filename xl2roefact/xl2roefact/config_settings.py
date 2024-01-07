"""Application configuration and setting parameters.  #TODO all of these are subject to documentation update (sectiune "RULES FOR INVOICE data in Excel")

NOTE english "README_me" before making changes:
* each parameter has a short help (lines starting with `#` character) - read it before changing that parameter
* do not change parametrs name as specified before equal (`=`) sign
* lists are enclosed in sqaured brackets (`[...]`) and items are separated by comma character (`,`)
* strings are enclosed in `"` characters
* if you want to clear a list (for example you do not wants any options inside) just let it as `<PARAMETR NAME> = []` - do not drop that parameter
* do not add supplementary parameters, they will not be used without software changes (also risk to induce potential errors)
* for calendaristic dates Excel cells use `date` format and change it as display option to show wanted format

NOTE romana "README_me" inainte de a face modificari:  #TODO all of these are subject to documentation update (sectiune "RULES FOR INVOICE data in Excel")
* fiecare parametru are un hep scurt (liniile ce incep cu caracterul `#`) - citi-l inainte de a modofica uun parametru
* nu schimbati numele parametrilor asa cum este el specificat inainte de semnul egal (`=`)
* listele sunt incluse intre paranteze drepte (`[...]`) si elementele lor sunt separate prin caracterul virgula (`,`)
* sirurile de caractere sunt incluse intre ghilimele (caracterul `"`)
* daca doriti stergerea unei listei (de ex daca nu doriti nici o optiune pentru acea lista) doar lasati acel parametru cu valoarea `[]` - nu stergeti in nici un caz acel parametru
* nu adaugati parametrii suplimentari (altii decit cei specificati aici), acestia nu vor fi utilizati fara a modifica aplicatia (de asemenea riscati sa induceti erori in cod)
* pentru datele calendaristice in celulul Excel a se utiliza formatul standard de data (`date`) si modificati formatul de afisare in formatul dorit pe factura tiparibila

Identification:
* code-name: `config_settings`
* copyright: (c) 2023 RENWare Software Systems
* author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""




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
# NOTE se presupune a fi la inceputul zonei cu datele furnizorului, deci se ca cauta dupa acelasi pattern
PATTERN_FOR_CUSTOMER_LEGAL_NAME = PATTERN_FOR_INVOICE_CUSTOMER_SUBTABLE_MARKER

# --- pattern-uri comune utilizate in regasirea informatiilor referitoare la partener (comune pentru client si furnizor)
# pattern pentru regasirea codului unic de inregistrare (sau Company ID in engleza)
PATTERN_FOR_PARTNER_ID = [
    "cui", "c.u.i",
    "cif", "c.i.f",
    "id",
]

...  # TODO: alte patternuri comune de adaugat aici (ex: RegCom, Adresa, IBAN, Banca, ...)


# FIXME: in factura Petrom nu ai nici ref furnizor nici client, ci ai numele firmelor lor, dar ai C.U.I.  #FIXME tried something @line 110...
# FIXME: ci alte texte COMPLET "OUT-OF-UDERSTANDING" chiar si pentru humans !
# TODO: decide something, most probably set this kind of issue in documentation section for: "RULES FOR INVOICE data in Excel"
# --- furnizor (supplier)
# pattern utilizat pentru a gasi aria (zona) cu datele furnizorului
PATTERN_FOR_INVOICE_SUPPLIER_SUBTABLE_MARKER: list[str] = [
    "furniz", "proprie",  # TODO: list patterns here
    "suppl", "owne",
]


