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
    * FINISHING_SOLUTION_TBD... publish `xl2roefact` package --> read `TODO_packaging.md`
-
* -#NOTE_PLAN_tbd... RDINV module ...just read file and identify big zones:
    * invoice header
        * [x] (DONE@0.1.12) invoice header - invoice number
        * [x] (DONE@231217piu_a) invoice header - issue date
        * [x] (DONE@0.1.13) invoice header - currency
        * [ ] invoice header - issuer / owner
        * [ ] invoice header - partners (supplier or customer) (#NOTE supplier will be good for `PayValidaBoa` to get suppliers invoices)



### 0.1.15 invoice issue date  (#TODO_WIP...)

* wip... WHEN RELEASE UPDATE `pyproject.toml`

* 231218piu_a installed `PDM` environment manager, updated `pyproject.toml` structures, nxt to create env, generate lock file...





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




### 0.1.7 `xl2roefact.RDINV` invoice items & metadata (231126 h05:00)

* **left OPEN ISSUES in this release** [piu@231126: marked on todo plan of `0.1.8` version]
    * [x] (CLOSED@231213) _file `xl2roefact/rdinv.py`, function `__mk_kv_invoice_items_area(...)`:_ `FIXME this will be identified in `invoice_header_area` ==> should be changed accordingly`
    * [ ] --> _file `xl2roefact\invoice_files/_PLAN_model_test_factura_generat_anaf.xml`, line 114:_ `<cbc:ID>S</cbc:ID> #FIXME clarify.me_ pare a fi TIPUL PRODUSULUI: (S)erviciu sau ??? (P)rodus sau ???`


* 231126piu_a item(s) line extensions == item VAT total, item VALUE total

* 231125piu_c changed dir `excel_invoices/` with `invoice_files/`

* 231125piu_b make a plan from `__model_test_factura_generat_anaf.xml` marking TODOs & DONE tags & renaming as `_PLAN_...idem...`

* 231125piu_a final review, complete find of invoice relevant columns and write them in `invoice` dict:
    * quantity (cbc:InvoicedQuantity),
    * VAT percent (cbc:Percent),
    * description (cbc:Name),
    * uom (cbc:unitCode),
    * unit price (cbc:PriceAmount),
    * currency (c:currencyID)

* 231224piu_a FIXED VAT calculation for lines which specify a VAT as 0% - USE CASE lines for other taxes like "acciza"... - still unsolved for very simplified invoices (see code line containing text "`_vat_percent` calculation should also")

* 231123piu_c `rdinv` module, defined function `libutils.isnumber(a_string: str) -> bool` to test is a string is valid as any kind of number

* 231123piu_b `rdinv` module, function to search for a list of string in a list items (suitable to identify useful / relevant invoice columns from Excel format) ==> **`__find_str_in_list(str_to_find: str, list_to_search: list)`**

* 231123piu_a prepared function `__mk_kv_invoice_items_area(...)` to transform `invoice_items_area` in "canonical JSON format" (as kv pairs)

* 231122piu_a  `invoice_items_area` & `meta_info` review, check and clean code

* 231121piu_a final `invoice` dict / JSON data: moved all effective data under key `"excel_data"` (preparing so for final storable invoice "real keys")

* 231119piu_b `invoice_items_area` set unknown rows header to `<current line number>.NOTE-<seq>`, where `seq` is an ordered sequence of letters (ie, resulting something like: `1.a, 1.b, ...`)
\* 231119piu_a closed:
    * [x] invoice `meta_info` area
    * [x] a more defined, clean & clear `invoice_items_area`
    * [x] add `last_processing_UTCtime` in `meta_info` dictionary
    * [x] written `invoice` dict to a JSON (`f-JSON` file, see doc: `https://apitoroefact.renware.eu/commercial_agreement/110-SRE-api_to_roefact_requirements.html#vedere-de-ansamblu-a-solutiei`)

* 231112piu_a refactor:
    *  [x] `base_proc` to `xl2roefact`
    *  [x] `BASE_PROC` to `xl2roefact`
    *  [x] update documentation
    *  [x] publish site

* 231109piu_a installed module `pylightxl` in base environment (ie, in project root) to allow modules calling from root for future web components & updated requirements.txt

* 231108piu_f RDINV (`rdinv.py`) secure for "unwanted crashes" errors (missing info) & clean code

* 2811080iu_e install `mkdocstrings`, update `mkdocs.yml` and create a markdown document for xl2roefact component (did) not succeeded search for 'FIXME temporary disabled because errs' ...longer_string_...

* 231108piu_d documented that `XLSX` is the only Excel file format supported (in `110-SRE-api_to_roefact_requirements.md`) & published site

* 231108piu_c xl2roefact (`xl2roefact.py`) transformed in class & parametrized worksheet name containing invoice ==> **class BaseProc()**

* 231108piu_b RDINV (`rdinv.py`) module set directories environment & open invoice

* 231108piu_a consolidate decomposition (from `231107piu_c`) ==> directory `.../xl2roefact/modules/`

* 231107piu_c transform decomposition (from `231107piu_b`) into complete Python modules (making directories for each)

* 231107piu_b created module files according to decomposition (specs doc `110-SRE-api_to_roefact_requirements.md`)

* 230107piu_a made a first DRAFT runnable CLI program with `Typer` (`https://typer.tiangolo.com/`) from `xls2xml.py` ==> `dist/xls2xml.exe`




### 0.1.6 commercial agreement OPTIONS document (231107 h07:00)

* 231106piu_e document for TECHNICAL agreement with (a) agreed options, (b) estimated deadlines ==> published i `commercial_agreement/` as `agreed_options.md` under "Options": menu
    * [x] (a.) for _APItoROefact_ system
    * [x] (b.) for _PayValidaBoa_ system
    * [x] (c.) publish updates



### 0.1.5 init component *xl2roefact* for CLI application (231106 h06:30)

* 231106piu_d published changed commercial documents
* 231106piu_c get test invoices: from client, a RENware one, a 3rd party one ==> directory `xl2roefact/test_data_and_specs/`
* 231106piu_b updated `doc_src/110-SRE-payments_validation_board_requirements.md` ref system decomposition & list of components
* 231106piu_a prepare environment for *xl2roefact* component:
    * [x] make a distinct Python-Windows environment in `xl2roefact/`
    * [x] set as git ignore the intended new environment directory: `.wenv_xl2roefact/`
    * [x] install required modules in new environment (`pylightxl` core module)
    * [x] create specific requirements file: `requirements_xl2roefact.txt`



### 0.1.4 Create system backbone structure (231105 h08:15)

* 231105piu_c create system backbone as directories structure (and initialized min with a `README_xxx.md` file):
    * `web_dashb_app/` for component *WEB_DASHB* (as renaming actual `api_to_roefact_app/`)
    * `xl2roefact/` for component *xl2roefact*
    * `data/` for component *SYSTEM_DB*
* 231105piu_b revisit and review existing directories and refactored:
    * `sysInit/` --> `sys_init/`
    * `setup/` --> `setup_web_sys/`
    * published site



### 0.1.3 Enhancing `payments_validation_board` technical proposal (231105 h05:30)

* 231105piu_a review, update & publish site `apitoroefact.renware.eu`
* 231104piu_i updated project README file
* 231104piu_h `payments_validation_board` updated commercial name of system to **PayValidaBoa** and related documentation files
* 231104piu_g update general considerations proposal doc ref using `UTC` date and times in applications databases
* 231104piu_f add new top level component for administration of: users, e-mails, signature certificates, roles
* 231104piu_e updated site server name to `apitoroefact.renware.eu` and `doc_src/CNAME` file
* 231104piu_d `payments_validation_board` technical proposal - first / draft components decomposition




### 0.1.2 Enhancing `APItoROefact` technical proposal (231104 10:30)

* 231104piu_c `APItoROefact` technical proposal: closed a discussion version




### 0.1.1 Elaborating technical proposal (231104 08:45)

* 231104piu_b got all commercial documents (including `110-SRE-general_requirements.md`) in directory `doc_src/commercial_agreement/`




### 0.1.0 System raw backbone (231104 07:00)

* 231104piu_a created first raw system backbone & directories structure















# Archived CHANGELOGs

* n/a


# [Release Notes](RELNOTE.md) #TODO this file should be created


