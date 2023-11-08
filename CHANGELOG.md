**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG

- For version code structure meaning see SDEVEN methodology document
- with _(F)_ are marked those changes that are features in order to be copied in a RELNOTE file and with _(B)_ bug fixes from versions released
- publishing is made under `publishing` branch
- `<PROJECT ROOT>/doc_src/` is the default starting location in a file path (if not clear from context) (**ATTN** - in production environment is `docs/`)
- `<WEB_ROOT>/` is the HTTP server root directory, as default `docs/` and supposed if no other parent is specified



## 0.1 -#TODO wip...


-#TODO ---------- short planning board ---------------------------------------------------------
* -ai exemplu de fact emisa catre Petrom in folder 100-ANA
* -ai un exemplu complet si complet agnostic (trimis Gigi) de factura format XML si PDF tiparit ca sa faci: (1) incarcare XML (2) geenrare PDF (3) compararea variantelor si identificarea schemei XSD + document specificatii ANAF ref sistemul E-Factura (PDF trimis Liviu)
-------------------------------------------------------------------------------------------------
* -#NOTE link Swagger servicii web: `https://mfinante.gov.ro/web/efactura/informatii-tehnice`
* -#NOTE link specif API incarcare fact: `https://mfinante.gov.ro/static/10/eFactura/upload.html#/EFacturaUpload/handleRequest`
-------------------------------------------------------------------------------------------------





### 0.1.7 #NOTE_wip... component *BASE_PROC* mocule *RDINV* for CLI application (...#NOTE_see_if_mk_only_RDINV_in_this_version...)

* wip...

* tbd... 231108piu_??? start RDINV module ...just read file and identify big zones:
    * [x] DONE@`231108piu_b` set directories environment & open invoice
    * invoice header - issuer (owner)
    * invoice header - partner (supplier or customer) (#NOTE supplier will be good for `PayValidaBoa` to get suppliers invoices)
    * invoice header - invoice identification (number, date, oth important as "non VAT payer")
    * invoice lines
    * invoice footer

* 231108piu_b RDINV module set directories environment & open invoice
* 231108piu_a consolidate decomposition (from `231107piu_c`) ==> directory `.../base_proc/modules/`
* 231107piu_c transform decomposition (from `231107piu_b`) into complete Python modules (making directories for each)
* 231107piu_b created module files according to decomposition (specs doc `110-SRE-api_to_roefact_requirements.md`)
* 230107piu_a made a first DRAFT runnable CLI program with `Typer` (`https://typer.tiangolo.com/`) from `xls2xml.py` ==> `dist/xls2xml.exe`









### 0.1.6 commercial agreement OPTIONS document (231107 h07:00)

* 231106piu_e document for TECHNICAL agreement with (a) agreed options, (b) estimated deadlines ==> published i `commercial_agreement/` as `agreed_options.md` under "Options": menu
    * [x] (a.) for _APItoROefact_ system
    * [x] (b.) for _PayValidaBoa_ system
    * [x] (c.) publish updates



### 0.1.5 init component *BASE_PROC* for CLI application (231106 h06:30)

* 231106piu_d published changed commercial documents
* 231106piu_c get test invoices: from client, a RENware one, a 3rd party one ==> directory `base_proc/test_data_and_specs/`
* 231106piu_b updated `doc_src/110-SRE-payments_validation_board_requirements.md` ref system decomposition & list of components
* 231106piu_a prepare environment for *BASE_PROC* component:
    * [x] make a distinct Python-Windows environment in `base_proc/`
    * [x] set as git ignore the intended new environment directory: `.wenv_base_proc/`
    * [x] install required modules in new environment (`pylightxl` core module)
    * [x] create specific requirements file: `requirements_base_proc.txt`



### 0.1.4 Create system backbone structure (231105 h08:15)

* 231105piu_c create system backbone as directories structure (and initialized min with a `README_xxx.md` file):
    * `web_dashb_app/` for component *WEB_DASHB* (as renaming actual `api_to_roefact_app/`)
    * `base_proc/` for component *BASE_PROC*
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


