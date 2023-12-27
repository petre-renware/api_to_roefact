**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG

- For version code structure meaning see SDEVEN methodology document
- with _(F)_ are marked those changes that are features in order to be copied in a RELNOTE file and with _(B)_ bug fixes from versions released
- publishing is made under `publishing` branch
- `<PROJECT ROOT>/doc_src/` is the default starting location in a file path (if not clear from context) (**ATTN** - in production environment is `docs/`)
- `<WEB_ROOT>/` is the HTTP server root directory, as default `docs/` and supposed if no other parent is specified



## 0.1 -#TODO wip...


- ---[ #TODO short planning board ]---------------------------------------------------------
* ai un exemplu complet si complet agnostic (trimis Gigi) de factura format XML si PDF tiparit ca sa faci: (1) incarcare XML (2) geenrare PDF (3) compararea variantelor si identificarea schemei XSD + document specificatii ANAF ref sistemul E-Factura (PDF trimis Liviu)

* -#NOTE link Swagger servicii web: `https://mfinante.gov.ro/web/efactura/informatii-tehnice`
* -#NOTE link specif API incarcare fact: `https://mfinante.gov.ro/static/10/eFactura/upload.html#/EFacturaUpload/handleRequest`
-------------------------------------------------------------------------------------------------





### #TODO_PLAN_TODO... `xl2roefact.RDINV` ???-[invoice issue date, invoice owner & partner?] (...)

* [ ] update documentation for:
    * [ ] `rdinv` module
    * [ ] `xl2roefact` CLI application
    * [ ] INVOICE TEMPLATE (`excel_invoice_template/` directory), doc `README_excel_invoice_rules.md`
    * [ ] use  Pydoc Markdown `https://niklasrosenstein.github.io/pydoc-markdown/usage/yaml/#yaml-example`
-
* left OPEN ISSUES on: `0.1.7` release (and drop them when fixed)
    * [ ] _file `xl2roefact\invoice_files/_PLAN_model_test_factura_generat_anaf.xml`, line 114:_ `<cbc:ID>S</cbc:ID> #FIXME clarify.me_ pare a fi TIPUL PRODUSULUI: (S)erviciu sau ??? (P)rodus sau ???`
-
* ... future intention is to make commands:
    * `config` - new... to set INTERACTIVELY configuration options (HINT: to use `Rich prompt`)
    * `xl2json - wip... RDINV` read Excel data and crate a JSON file (with map to convert to RO-EFact XML) with invoice data,
    * `json2xml - WRXML`,
    * `json2pdf` - new...,
    * `xml2roefact - LDXML`
    * create a **`build.bat`** & include in `MSI` package 'data' directories as: `excel_invoice_template/`, empty `invoice_files/` (see `cx-Freeze`, options `--directories` of `bdist_msi`cmd, option `--include_files` of `build_exe`cmd, ref URL: `https://cx-freeze.readthedocs.io/en/latest/setup_script.html`)
    * other commands enumerated on `https://apitoroefact.renware.eu/commercial_agreement/110-SRE-api_to_roefact_requirements.html#componenta-xl2roefact`
    * PACKAGE SOLUTION:
        * [ ] publish `xl2roefact` package --> read `TODO_packaging.md`
        * [x] (DONE@231229piu_a) make some useful PDM scripts (ref `pyproject.toml`, table section `[tool.pdm.scripts]`) like build commands for:
        * [x] (DONE@0.1.17) make a PDM build: OK, currently is done @ each release, results ==> `.../dist/xl2roefact-0.1.15-py3-none-any.whl` & `.../dist/xl2roefact-0.1.15.tar.gz`
-
* -#NOTE_PLAN_tbd... RDINV module ...just read file and identify big zones:
    * invoice header
        * [x] (DONE@0.1.12) invoice header - invoice number
        * [x] (DONE@231217piu_a) invoice header - issue date
        * [x] (DONE@0.1.13) invoice header - currency
        * [ ] invoice header - supplier (`<cac:AccountingSupplierParty>`)
        * [ ] invoice header - customer (`<cac:AccountingCustomerParty>`)



### 0.1.18 invoice partners customer  (#TODO_WIP...)

* wip... WHEN RELEASE UPDATE `pyproject.toml`
* tbd... invoice header - supplier (`<cac:AccountingSupplierParty>`)

* 231227piu_a generated a first draft of markdown documentation:
    * [x] used Pydoc Markdown @ `https://niklasrosenstein.github.io/pydoc-markdown/usage/yaml/#yaml-example`
    * [x] results ==> `<PJ_ROOT>/xl2roefact/doc/generated_810.05a-xl2roefact_component.md`
    * [x] created PDM shell command `pdm run` (command just for quick remembers: `pydoc-markdown -I xl2roefact --render-toc >doc/generated_810.05a-xl2roefact_component.md`)

* 231226piu_b reviewed `xl2roefact` all "in use" code and updated `docstrings`

* 231226piu_a made some useful PDM scripts (ref `pyproject.toml`, table section `[tool.pdm.scripts]`) like build commands for:
    * [x] **`pdm build_wheel`** Python package,
    * [x] **`pdm build_msi`** MSI package,
    * [x] **`pdm build_all`** build all packages
    * [x] **`pdm xl2roefact`** run xl2roefact command
    * [x] updated `doc/810.05a-xl2roefact_component.md`









### 0.1.17 fixed all application & package running standard ways (231224 h05:30)

* RELEASES:
    * `.<PROJECT>/xl2roefact/dist/xl2roefact-0.1.17-win64.msi`
    * `<PROJECT>/xl2roefact/dist/xl2roefact-0.1.17.tar.gz`
    * `<PROJECT>/xl2roefact/dist/xl2roefact-0.1.17-py3-none-any.whl`

* 231224piu_a made cli app to run as: Python package main app (`python -m xl2roefact`) and as script (`python xl2roefact.py`) while still letting the Python library `xl2roefact` as importable and use in a programmatic way:
    * [x] make `.../xl2roefact/app_cli.py` (from actual `.../xl2roefact/__main__.py`) which is complete code of CLI app plus a `run()` function that just launch it
    * [x] make `.../xl2roefact/__main__.py` that just import `app_cli` for `run()` function and call it
    * [x] change actual `<xl2roefact ROOT/>xl2roefact.py` to import `xl2roefact.app_cli` for `run()` function and call it
    * [x] test for MSI package builds ref `<xl2roefact ROOT/>xl2roefact.py`
    * [x] clean code, test and close issue:
        * `python xl2roefact.py [OPTIONS] COMMAND [ARGS]...`
        * `python -m xl2roefact [OPTIONS] COMMAND [ARGS]...`

* 231223piu_a multiple changes ref main code: `xl2roefact.py` and library `xl2roefact`, MAINLY created `xl2roefact/__main__.py` as normal of xl2roefact.py






# 0.1.16 improving Excel kv-data search with "IN-LABEL" method (231222 h07:00)

* 231222piu_b build packages for:
    * [x] application deployment package ==> `dist/0.1.13-xl2roefact-0.1-win64.msi`
    * [x] cleaned, tested, created packages (saved to ==> `.../880-RLSE/880.90-RLSE Source Code Archives`)
    * [x] updated `pyproject.toml`

* 231222piu_a refactor `rdinv.__get_excel_data_at_label(...)` to search in label (named "IN-LABEL" method)

* 231220piu_b made a first PDM build: [@ 231220 h09:55] ==> test PASS (both created files in `dist/` was "git-ignored")

* 231220piu_b refactored `rdinv(...)` section "section for search of `invoice_items_area` ..." to use `__get_excel_data_at_label(...)` function`

* 231220piu_a refactored `rdinv.__get_excel_data_at_label(...)` for returned "label_position" key`

* 231219piu_a update `rdinv.__get_excel_data_at_label(...)` to return found label value in dictionary as key `"label_value"`

* 231218piu_c `PDM` environment manager, updated `pyproject.toml` structures ref package building, still preps to create env, generate lock file...

* 231218piu_b CLI application, fixed bug of print settings when deployed from a package (command: `xl2roefact.py settings`)

* 231218piu_a installed `PDM` environment manager, updated `pyproject.toml` structures, nxt to create env, generate lock file...






### 0.1.15 updated solution portal `http://invoicetoroefact.renware.eu/` (231222 h05:00)

* 231222piu_a updated CNAME to `invoicetoroefact.renware.eu`






### 0.1.14 invoice issue date  (231217 h07:00)

* 231217piu_b build packages for:
    * [x] application deployment package ==> `dist/0.1.13-xl2roefact-0.1-win64.msi`
    * [x] cleaned, tested, created packages (saved to ==> `.../880-RLSE/880.90-RLSE Source Code Archives`)
    * [x] updated `pyproject.toml`

* 231217piu_a invoice header, issue date (&& ATTN pendulum raise error, see `rdinv.py` line #17, ==> MAYBE JUST TRY `Arrow` or standard `datetime`)

* 231216piu_a review, improve & clean code for: `xl_invoices/config_settings.py`, `xl_invoices/rdinv.py`

* 231215piu_b FIXED configs loaded from config_settings: `rdinv` module load (init) all constants as global variables (because they are subject to change / "improve" values as reading Excel file, for example `DEFAULT_CURRENCY`)

* 231215piu_a changed dir name **`xl_invoice_modules/`** to `xl_invoices` or classic `xl2roefact`  as this will be the package name. This is a Python official RECOMMENDATION not a constraint

* 231214piu_a made xl2roefact Python standard package (moved `xl2roefact` modules to a dedicated directory (`xl_invoice_modules/`) with intention to publish package)






### 0.1.13 invoice currency (231213 h07:00)

* 231213piu_b build packages for:
    * [x] application deployment package ==> `dist/0.1.13-xl2roefact-0.1-win64.msi`
    * [x] cleaned, tested, created packages (saved to ==> `.../880-RLSE/880.90-RLSE Source Code Archives`)
* 231213piu_a get invoice header - invoice currency






### 0.1.12 invoice number (231212 07:30)

* 231212piu_b write canonical form (as @invoice lines, see line ~122) ==> `invoice["Invoice"]["cbc_ID"]` and released `0.1.12-xl2roefact-0.1-win64.msi`

* 231212piu_a `rdinv.rdinv()` invoice header, invoice number as: `{"value": ..., "location": (row..., col...)}`

* 231211piu_b `rdinv.rdinv()` create a function special to get "one key Excel values", like invoice number or invoice issue date.  Signature:
    - `pattern_to_search_for: list[str]` - for inv number will pass the `PATTERN_FOR_INVOICE_NUMBER_LABEL`
    - `area_to_scan: list[start_cell, end_cell]` - for inv number will pass `(invoice_header_area["start_cell"], invoice_header_area["end_cell"])`
    - targeted_tye: type - what type expect (will try to convert to, if cannot will return str)

* 231211piu_a updated `config_settings.py` ref how to find it: string labels to search, direction to search effective info starting from label

* 231210piu_a localized and marked areas for invoice header (`invoice_header_area`) & invoice footer (`invoice_footer_area`) ==> dicts for header and footer with structure `{ start_cell = (row, col), end_cell = (row, col) }`






### 0.1.11 (231209 h08:00)

* 231209piu_c build packages for:
    * [x] application deployment package ==> `dist/0.1.11-xl2roefact-0.1-win64.msi`
    * [x] excel invoice template package ==> `dist/0.1.11-excel_invoice_template.zip`
    * [x] cleaned, tested, created packages (saved to ==> `.../880-RLSE/880.90-RLSE Source Code Archives`)

* 231209piu_b **fixed `xl2roefact` CLI options, help, defaults, short names** and __STABILIZED EXECUTION__

* closed `231209piu_a` more actions:
    * changed `README.md`: translated to RO, updated installation & usage information
    * dropped old, obsolete deployment packages
    * test PASS

* 231208piu_b add an INVOICE TEMPLATE (`excel_invoice_template/invoice_template_CU_tva.xlsx`) as deliverable with application

* 231208piu_a review, cleaning and formatting code (generalized & moved some debug-verbose code from `rdinv` to `xl2roefact.xl2json`), test PASS
* 231207piu_b cleaned `rdinv` of "...for debug purposes..." prints, test PASS

* 231207piu_c reviewed and updated `xl2roefact`: README, LICENSE, pyproject.toml




### 0.1.10 command interface improved, `msi` package building, invoice template & updated documentation (231207 h12:00)

* 231207piu_b build a `MSI` package for `0.1.10` version ==> **`0.1.10-xl2roefact-0.1-win64.msi`**, also installed `Python 3.11` + `cx-Freeze` & updated `requirements_xl2roefact.txt`

* 231207piu_a FIXED errors due to Excel files directory duplication in `xl2roefact` & `rdinv()`

* 231206piu_a clean code for `rdinv` & `xl2roefact`, reviewed cnd closed some open issues (todos, notes, ...)

* 231205piu_b made a directory for INVOICE TEMPLATE (`excel_invoice_template/`) to be delivered with solutions "for who need a simple template", also write here a `README_excel_invoice_rules.md` to describe all required conditions in order to be "RECOGNIZED & TRANSLATED to JSON"

* 231205piu_a change all solution to use `rich` library instead of `colorama` (Rich library ref `https://rich.readthedocs.io/en/stable/index.html`)
    * [x] drop all `from colorama import Fore, Back, Style`
    * [x] add new `from rich import print`
    * [x] update all places where `{Fore....}` with `[...]` as:
        * [x] `{Fore.YELLOW}` with `[yellow]`
        * [x] `{Fore.GREEN}` with `[green]`
        * [x] `{Fore.MAGENTA}` with `[magenta]`
        * [x] `{Fore.BLUE}` with `[blue]`
        * [x] `{Fore.CYAN}` with `[cyan]`
        * [x] `{Fore.RED}` with `[red]`
    * [x] change all `typer.echo` with `print`
    * [x] update all places where `{Style.RESET_ALL}` with `[/]`

* 231204piu_c build new executable and installer ==> `dist/0.1.10.231204piu_a-xl2roefact-0.1-win64.msi`

* 231204piu_b created `./doc/` renamed and moved all documentation documents - intention to keep clean `xl2roefact root`

* 231204piu_a `xl2roefact xl2json` check rdinv() result and if return False, ONLY print a message of "INFO note" then continue with next file (the effective error was print by module itself) && build a new executable package ==> `dist/0.1.10.231204piu_a-exe.win-amd64-3.10.zip`




### 0.1.9 `xl2roefact.RDINV` running executable and distribution kit (231203 h07:00)

* 231103piu_b releasing ==> made `dist/0.1.9-exe.win-amd64-3.10.zip` with executable file

* 231103piu_a `xl2roefact.py` more updates:
    * [x] set verbose flag for debugging mode
    * [x] made `file_name` argument as file(s) to be processed with wildcards like Python standard function `os.glob.glob()` (reference here `https://docs.python.org/2/library/glob.html`)
    * [x] build a new fresh executable in `build/exe.win-amd64-3.10/`

* 231202piu_b `xl2roefact.py` started a skeleton for `file_name` argument - see code-in-file @"TODO here to use `excel_files_directory` + / + `file_name` to find all files and process them in a loop"

* 231202piu_a build complete `cxFreeze` configuration in order to build Windows executable and installer package (as `msi` package):
    * [x] create a minimal setup (`setup.py`)
    * [x] create `build/` directory with all building commands for _xl2roefact_ app: `python setup.py build` (see official doc here `https://cx-freeze.readthedocs.io/en/latest/setup_script.html`)
    * **CONCLUSION** `msi` package OK, `exe` file NOK - see `setup.py` for a detailed comment marked `NOTE-[piu@231202]`




### 0.1.8 improved application structure and first executable release (231201 h07:30)

* 231201piu_b installed `cx-Freeze` library and build a new Windows executable, update documentation - need future improvement to make `msi` package, but TEST PASSED and works perfectly

* 231201piu_a improve CLI application structure (`xl2roefact.py`) and commands: `xl2json`, `about`

* 231130piu_a `xl2roefact.py`, `——excel_files_directory`: option, make it of type pathlib.Path, dealut remain as is, validators; is dir, exists, writable, readable, resolve_path

* 231129piu_b updated `xl2roefact.py` (main application) changed command `run` --> `xl2json` and add parameter `excel_files_directory` (future intention is to make commands: `xl2json - RDINV`, `json2xml - WRXML`, `json2pdf`, `xml2roefact - LDXML`)

* 231129piu_a adopted new REN invoice template (test with data from RENF-1004)

* 231128piu_b made `config_settings.py` for general application configuration purposes and an application command (`xl2roefact settings`) to print them

* 231128piu_a made `xl2roefact.py` (main library file) as CLI executable structure (with `Typer` library)

* 231127piu_c introduced **key `Invoice`** in  invoice JSON generated structure (also representing the "entity" in XML representation)

* 231127piu_b module `rdinv` crated a distinct function for building of `meta_info` key (main `invoice` dictionary)

* 231127piu_a created in invoice JSON map JSON key --> XML property (`meta_info["map_JSONkeys_XMLtags"]`) as `list of tuple(JSONkey: str, XMLtag: str)`

* 231127piu_a created draft data models for: invoice (exportable as JSON and XML) and other entities (owner, customer) ==> `data_models.py`






# Archived CHANGELOGs

* [0.1.7 `xl2roefact.RDINV` invoice items & metadata + *OPEN ISSUES*](./changelog_history/CHANGELOG-0.1.7.md)
* [0.1.6 commercial agreement OPTIONS document](changelog_history/CHANGELOG-0.1.6.md)
* [0.1.5 init component *xl2roefact* for CLI application](./changelog_history/CHANGELOG-0.1.5.md)
* [0.1.4 Create system backbone structure](./changelog_history/CHANGELOG-0.1.4.md)
* [0.1.3 Enhancing `payments_validation_board` technical proposal](./changelog_history/CHANGELOG-0.1.3.md)
* [0.1.2 Enhancing `APItoROefact` technical proposal](./changelog_history/CHANGELOG-0.1.2.md)
* [0.1.1 Elaborating technical proposal](./changelog_history/CHANGELOG-0.1.1.md)
* [0.1.0 System raw backbone](./changelog_history/CHANGELOG-0.1.0.md)







# [Release Notes](RELNOTE.md) #TODO this file should be created

* wip... [not_yet_created... 0.1](./changelog_history/...)
