# Table of Contents

* [app\_cli](#app_cli)
  * [about](#app_cli.about)
  * [settings](#app_cli.settings)
  * [xl2json](#app_cli.xl2json)
* [chkisld](#chkisld)
  * [chkisld](#chkisld.chkisld)
* [chkxml](#chkxml)
  * [chkxml](#chkxml.chkxml)
* [config\_settings](#config_settings)
  * [DEFAULT\_CURRENCY](#config_settings.DEFAULT_CURRENCY)
* [ldxml](#ldxml)
  * [ldxml](#ldxml.ldxml)
* [libutils](#libutils)
  * [isnumber](#libutils.isnumber)
  * [find\_str\_in\_list](#libutils.find_str_in_list)
* [rdinv](#rdinv)
  * [SYS\_FILLED\_EMPTY\_CELL](#rdinv.SYS_FILLED_EMPTY_CELL)
  * [rdinv](#rdinv.rdinv)
* [wrxml](#wrxml)
  * [wrxml](#wrxml.wrxml)
* [\_\_init\_\_](#__init__)
* [\_\_main\_\_](#__main__)

<a id="app_cli"></a>

# app\_cli

**xl2roefact.app_cli**: the command line application for all xl2roefact functionalities.

Identification:
    * code-name: `xl2roefact`
    * copyright: (c) 2023 RENWare Software Systems
    * author: Petre Iordanescu (petre.iordanescu@gmail.com)

Deployments:
    * Windows:  MSI installer with EXE application.
    * Linux: `xl2roefact` executable shell as wrapper for `xl2roefact.py`.

Specifications:
    * command general format: `xl2roefact [file(s)-to-convert] COMMAND [OPTIONS]`.
    * help: `xl2roefact [COMMAND] --help`.

<a id="app_cli.about"></a>

#### about

```python
@app_cli.command()
def about()
```

provide a short application description.

<a id="app_cli.settings"></a>

#### settings

```python
@app_cli.command()
def settings()
```

display application configuration parameters and settings that are subject to be changed by user.

<a id="app_cli.xl2json"></a>

#### xl2json

```python
@app_cli.command()
def xl2json(
    file_name: Annotated[
        str, typer.Argument(
            help="files to process (wildcards allowed)")] = "*.xlsx",
    excel_files_directory: Annotated[
        Path,
        typer.Option("--files-directory",
                     "-d",
                     exists=True,
                     file_okay=False,
                     dir_okay=True,
                     writable=True,
                     readable=True,
                     resolve_path=True,
                     help="directory to be used to look for Excel files"),
    ] = "invoice_files/",
    verbose: Annotated[
        bool,
        typer.
        Option("--verbose", "-v", help="show detailed processing messages"),
    ] = False)
```

extract data from an Excel file (save data to JSON format file with the same name as original file but `.json` extension).

<a id="chkisld"></a>

# chkisld

<a id="chkisld.chkisld"></a>

#### chkisld

```python
def chkisld()
```

CHKISLD - modul de verificare a starii de incarcare a unei facturi emise

Identification:
    code-name: `chkisld`
    copyright: (c) 2023 RENWare Software Systems
    author: Petre Iordanescu (petre.iordanescu@gmail.com)

Specifications:
    document: `110-SRE-api_to_roefact_requirements.md` section `Componenta xl2roefact`
    INTRARI: fisier `f-XLSX` sau numarul / cheia / codul facturii
    IESIRI: valoarea echivalent `TRUE` daca factura a fost deja incarcata sau valoare echivalent `FALSE` daca factura nu a fost incarcata

<a id="chkxml"></a>

# chkxml

<a id="chkxml.chkxml"></a>

#### chkxml

```python
def chkxml()
```

CHKXML - modul de validare a facturii in sistemul ANAF E-Factura

Identification:
    code-name: `chkxml`
    copyright: (c) 2023 RENWare Software Systems
    author: Petre Iordanescu (petre.iordanescu@gmail.com)

Specifications:
    document: `110-SRE-api_to_roefact_requirements.md` section `Componenta xl2roefact`
    INTRARI: fisier `f-XML`
    IESIRI: raport cu eventualele erori de validare

<a id="config_settings"></a>

# config\_settings

Application configuration and setting parameters.  `TODO` all of these are subject to documentation update (sectiune "RULES FOR INVOICE data in Excel")

NOTE english "README_me" before making changes:
    - each parameter has a short help (lines starting with `#` character) - read it before changing that parameter
    - do not change parametrs name as specified before equal (`=`) sign
    - lists are enclosed in sqaured brackets (`[...]`) and items are separated by comma character (`,`)
    - strings are enclosed in `"` characters
    - if you want to clear a list (for example you do not wants any options inside) just let it as `<PARAMETR NAME> = []` - do not drop that parameter
    - do not add supplementary parameters, they will not be used without software changes (also risk to induce potential errors)
    - for calendaristic dates Excel cells use `date` format and change it as display option to show wanted format

NOTE romana "README_me" inainte de a face modificari:  `TODO` all of these are subject to documentation update (sectiune "RULES FOR INVOICE data in Excel")
    - fiecare parametru are un hep scurt (liniile ce incep cu caracterul `#`) - citi-l inainte de a modofica uun parametru
    - nu schimbati numele parametrilor asa cum este el specificat inainte de semnul egal (`=`)
    - listele sunt incluse intre paranteze drepte (`[...]`) si elementele lor sunt separate prin caracterul virgula (`,`)
    - sirurile de caractere sunt incluse intre ghilimele (caracterul `"`)
    -daca doriti stergerea unei listei (de ex daca nu doriti nici o optiune pentru acea lista) doar lasati acel parametru cu valoarea `[]` - nu stergeti in nici un caz acel parametru
    - nu adaugati parametrii suplimentari (altii decit cei specificati aici), acestia nu vor fi utilizati fara a modifica aplicatia (de asemenea riscati sa induceti erori in cod)
    - pentru datele calendaristice in celulul Excel a se utiliza formatul standard de data (`date`) si modificati formatul de afisare in formatul dorit pe factura tiparibila

Identification:
    * code-name: `config_settings`
    * copyright: (c) 2023 RENWare Software Systems
    * author: Petre Iordanescu (petre.iordanescu@gmail.com)

<a id="config_settings.DEFAULT_CURRENCY"></a>

#### DEFAULT\_CURRENCY

---------------------------------------------------------------------------------------------------------------------------
__NOTE: "pattern-uri" (sabloane) de identificare si regasire a datelor folositi de__

__  comanda `xl2json` reprezentind functionalitatea de extragere a datelor din Excel si exportul lor in formatul JSON (modulul `rdinv)__

---------------------------------------------------------------------------------------------------------------------------

<a id="ldxml"></a>

# ldxml

<a id="ldxml.ldxml"></a>

#### ldxml

```python
def ldxml()
```

LDXML - modul de incarcare a facturii in sistemul ANAF E-Factura

Identification:
    code-name: `ldxml`
    copyright: (c) 2023 RENWare Software Systems
    author: Petre Iordanescu (petre.iordanescu@gmail.com)

Specifications:
    document: `110-SRE-api_to_roefact_requirements.md` section `Componenta xl2roefact`
    INTRARI: fisier `f-XML`
    IESIRI: raport cu validarea si identificatorul incarcarii

<a id="libutils"></a>

# libutils

libutils: general utilities library.

Identification:
    * code-name: `libutils`
    * copyright: (c) 2023 RENWare Software Systems
    * author: Petre Iordanescu (petre.iordanescu@gmail.com)

Components:
    `isnumber(a_string: str) -> bool`
        Test a string if it could be used as number (int or float)
    `find_str_in_list(list_of_str_to_find: list, list_to_search: list) -> int`
        Search more strings (ie, a list) in list of strings

<a id="libutils.isnumber"></a>

#### isnumber

```python
def isnumber(a_string: str) -> bool
```

test if a string is valid as any kind of number.

**Arguments**:

- ``a_string`` - input string.
  

**Returns**:

  `True` if input string is valid as any kind of number, orherwise `False`.

<a id="libutils.find_str_in_list"></a>

#### find\_str\_in\_list

```python
def find_str_in_list(list_of_str_to_find: list, list_to_search: list) -> int
```

find a substring from `list_of_str_to_find` in elements of `list_to_search`.

**Arguments**:

- ``list_of_str_to_find`` - list of strings to search for.
- ``list_to_search`` - liste where to search for substrings.
  

**Returns**:

- ``index`` - the index of list item which contains `str_to_find` (first found) or `None` if not found.

<a id="rdinv"></a>

# rdinv

rdinv: modul de procesare a fisierului Excel ce contine factura si colectare a datelor aferente.

Formatul acceptat fisier Excel este `XLSX`.

    Identification:
        code-name: `rdinv`
        copyright: (c) 2023 RENWare Software Systems
        author: Petre Iordanescu (petre.iordanescu@gmail.com)

    Specifications:
        document: `110-SRE-api_to_roefact_requirements.md` section `Componenta xl2roefact`
        INTRARI: fisier format XLSX ce contine factura emisa (cod: `f-XLSX`)
        IESIRI: fisier format JSON imagine a datelor facturii (cod: `f-JSON`)

<a id="rdinv.SYS_FILLED_EMPTY_CELL"></a>

#### SYS\_FILLED\_EMPTY\_CELL

this is not a changeale constant

<a id="rdinv.rdinv"></a>

#### rdinv

```python
def rdinv(file_to_process: str,
          invoice_worksheet_name: str = None,
          *,
          debug_info: bool = False) -> dict
```

read Excel file for invoice data.

Produce a dictionary structure + JSON file with all data regarding read invoice: canonical KV data, meta data, map to convert to XML and original Excel data.

**Arguments**:

- ``file_to_process`` - the invoice file (exact file with path).
- ``invoice_worksheet_name`` - the worksheet containing invoice.
- ``debug_info`` - positional only, show debugging information, default `False`.
  

**Returns**:

- ``dict`` - the invoice extracted information from Excel file as `dict(Invoice: dict, meta_info: dict, excel_original_data: dict)`  `TODO` subject of documentation update.
  
  NOTE ref important variables:
  * `db: pylightxl object`: EXCEL object with invoice (as a whole)
  * `ws: pylightxl object`: WORKSHEET object with invoice

<a id="wrxml"></a>

# wrxml

<a id="wrxml.wrxml"></a>

#### wrxml

```python
def wrxml()
```

WRXML - modul de generare a fisierului format XML

Identification:
    code-name: `wrxml`
    copyright: (c) 2023 RENWare Software Systems
    author: Petre Iordanescu (petre.iordanescu@gmail.com)

Specifications:
    document: `110-SRE-api_to_roefact_requirements.md` section `Componenta xl2roefact`
    INTRARI: fisier `f-JSON`
    IESIRI: fisier format XML conform cerintelor si sistemului ANAF E-Factura (cod: `f-XML`)

<a id="__init__"></a>

# \_\_init\_\_

<a id="__main__"></a>

# \_\_main\_\_

**xl2roefact.__main__**: Python package standard file to assure run as `python -m xl2roefact`.

Identification:
    * code-name: `__main__`
    * copyright: (c) 2023 RENWare Software Systems
    * author: Petre Iordanescu (petre.iordanescu@gmail.com)

Deployments:
    * Windows:  MSI installer with EXE application.
    * Linux: `xl2roefact` executable shell as wrapper for `xl2roefact.py`.

Specifications:
    * command general format: `python -m xl2roefact [OPTIONS] COMMAND [ARGS]... `.
    * help: `python -m xl2roefact --help`.

