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
    * [ ] INVOICE TEMPLATE (`excel_invoice_template/` directory), doc `README_excel_invoice_rules.md` first ref "Cum sa utilizeti sablonul, reguli de urmat in completarea datelor"
    * [x] (DONE: 0.1.18-231227piu_a) used Pydoc Markdown `https://niklasrosenstein.github.io/pydoc-markdown/usage/yaml/#yaml-example`
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
        * [x] (DONE: 0.1.18-231226piu_a) make some useful PDM scripts (ref `pyproject.toml`, table section `[tool.pdm.scripts]`) like build commands for:
        * [x] (DONE: 0.1.17) make a PDM build: OK, currently is done @ each release, results ==> `.../dist/xl2roefact-0.1.15-py3-none-any.whl` & `.../dist/xl2roefact-0.1.15.tar.gz`
-
* -#NOTE_PLAN_tbd... RDINV module ...just read file and identify big zones:
    * invoice header
        * [x] (DONE: 0.1.12) invoice header - invoice number
        * [x] (DONE: 0.1.14-231217piu_a) invoice header - issue date
        * [x] (DONE: 0.1.13) invoice header - currency
        * [ ] invoice header - supplier (`<cac:AccountingSupplierParty>`)
        * [ ] #NOTE...wip... invoice header - customer (`<cac:AccountingCustomerParty>`)






### 0.1.19.dev invoice customer and partial invoice total values calculations  (#NOTE TODO: wip...)

* -#TODO_ASAP after 0.1.19 consider **0.1.0** where to update main portal doc and change:
    - all `APItoROefact` to **`xl2roefact`** as meaning **`Excel invoices and RO EFact`**
    - ck CNAME if points to new DNS name: `https://invoicetoroefact.renware.eu/`
    - make a global link to GitHub Issues refined for 2 entries: *bugs* & *suport si documentatie utilizare*

* wip... WHEN RELEASE UPDATE `pyproject.toml`, `pdm build_doc` & `pdm build_all`

* tbd... `def_inv_dir` issue - comments in `app_cli.py`, function `xl2json(...)`
    * ... ++ `about` command to get version from `xl2roefact/__version__.py`
    * ... ++ `xl2json` command make Option for `--version` or implement just as distinct commanda (ie, `xl2roefact --version`) - see Typer doc @ parameter types for examples ref `--version`

* tbd... invoice customer search for other keys: "reg com", "bank / IBAN / cont", ... (area saved in `_area_to_search`)

* tbd... clean code `rdinv()` from customer area identification, line 204

* tbd..  next key to find: `cac:PostalAddress --> cac:Country`

* tbd... `xl2roefact/setup.py`ref get app version from file when build EXE/MSI (#TODO **iss001**) uncomment code, test and release / ALSO CHK IF IS ABLE TOVAUTO TAKE VERSION from pyproject.toml AS IS NOW FOR PDM

* 240110piu.a reviewed & updated `xl2roefact` package `README.md` + `xl2roefact/__version__.py` with an app logo and for text mistyping bugs

* 240108piu_c changed `pyproject.toml` for auto update package version from file `xl2roefact/__version__.py` (see also opiss 240108piu_b)

* 240108piu_b created `xl2roefact/__version__` file that contains variable `__version__` with INTENTION to use in `pyproject.toml` for app version key (in a future issue)

* #FIXME to test all up here #FIXME

* 240108piu_a more items:
    * `config_settings.py` created entry `PATTERN_FOR_PARTNER_ADDRESS` & updated `rdinv` module in constants area
    * add comments in `app_cli.py` ref `def_inv_dir` issue &&...
    * updated environment dependencies and installed `pyinstaller` development package with intention to make "single EXE" application to be able to run "from USB stick"

* 240107piu_a reviewed `xl2roefact` package `README.md`:
    - (c) explained proposed & promoted directory structure used by CLI application
    - (b) short invoice JSON file structure
    - (a) created first version of tutorial section

* 240106piu_a invoice customer search and persist for "RegistrationName"










### 0.1.18.dev invoice customer CUI partial invoice total values calculations  (240105 h08:00)

* 240105piu_c updated `xl2roefact` package `README.md` file (with new sections for intro to Excel invoice content rules, tutorial TODO, reference to technical doc)

* 240105piu_b invoice customer search and persist for "CUI"

* 240105piu_a `rdinv.def get_excel_data_at_label(...)` changed strategy for DOWN search-method made it optional with default True (useful for Partners set-of KVs where is supposed to be or IN-LABEL or in RIGHT but NOT DOWN because there is a list of KVs not just one placed anywhere in Excel doc)  #TODO tgis is subject of doc update

* 240103piu_d `rdinv.def get_excel_data_at_label(...)` changed strategy for IN-LABEL search-method to return all string except first word (supposed to be label) separated by space character (old strategy was to get only last work from all string)

* 240103piu_c ref invoice customer created in `config_settings.py` PATTERNs for search keys `PATTERN_FOR_PARTNER_ID` (CUI or ID), `PATTERN_FOR_PARTNER_LEGAL_NAME`

* 240103piu_b calculated item lines VAT amount as `cac_InvoiceLine.LineVatAmmount` as raw float value (not rounded to be able to round just invoice TOTAL)

* 240103piu_a `rdinv.rdinv()` updated JSON -- XML map (part of function `_build_meta_info_key(...)`)

* 240102piu_a `rdinv.rdinv()` upd & improved a clear Customer specific XML compliant structure. Targeted this XML structure:
                ```
                    <cac:PartyLegalEntity>
                        <cbc:RegistrationName>IORDANESCU PETRE PFA</cbc:RegistrationName>
                        <cbc:CompanyID>21986376</cbc:CompanyID>
                    </cac:PartyLegalEntity>
                ```

* 240101piu_a clean useless & obsolete project files, test new full build (MSI, Python wheel, documentation) ==> PASS OK

* 231229piu_a invoice customer (`<cac:AccountingCustomerParty>`) detect & set area to search for specific keys (like CUI, RegCom, IBAN, ...)
    * [x] 1. established AREA TO SEARCH for PARTNER data an `_area_to_search` (~line 244)
    * [x] 2. updated `config_settings.py` changed: (for a clear understating of constant scope, because will follow others for specific keys like: "reg com", "CUI", "bank / IBAN / cont", ...)
        - `PATTERN_FOR_INVOICE_CUSTOMER_LABEL` --> `PATTERN_FOR_INVOICE_CUSTOMER_SUBTABLE_MARKER`
        - `PATTERN_FOR_INVOICE_SUPPLIER_LABEL` --> `PATTERN_FOR_INVOICE_SUPPLIER_SUBTABLE_MARKER`
    * [x] 3. set-persist `_area_to_search` for next steps & save its key-info in associated invoice JSON (for further references) - `rdinv()` ~line 239
    * [x] 4. updated main xl2roefact README.md document ref latter changes and app structuring, concepts, ...(ideas evolving :)...
    * [x] 5. done code for `cac_AccountingSupplierParty` key by iterating full `invoice_header_area["customer_area"]` structure

* 231228piu_a improved documentation generation:
    * [x] updated all modules docstring(s) to a right markdown representation in generated documentation (ex: when use bullets THEN DO NOT indent at 1st level)
    * [x] __@IMP_NOTE:__ Changed generated documentation file to `doc/810.05a-xl2roefact_DLD_specs.md` and referred in main `doc/810.05a-xl2roefact_component.md` as this being a final solution for whole project documentation (that generated with `mkdocs`)
    * [x] updated `pyproject.toml, [tool.pdm.scripts]` table with new generated doc file name (810.05a-xl2roefact_DLD_specs.md)

* 231227piu_b updated `xl2roefact.rdinv` module ref dropped `_` chars from internal function names to allow doc generation by PyDoc until will produce a YAML file for PyDoc generator (where will be able to specify concrete list of objects regarding their names)

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






### 0.1.17.dev fixed all application & package running standard ways (231224 h05:30)

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






### 0.1.16.dev improving Excel kv-data search with "IN-LABEL" method (231222 h07:00)

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






### 0.1.14.dev invoice issue date  (231217 h07:00)

* 231217piu_b build packages for:
    * [x] application deployment package ==> `dist/0.1.13-xl2roefact-0.1-win64.msi`
    * [x] cleaned, tested, created packages (saved to ==> `.../880-RLSE/880.90-RLSE Source Code Archives`)
    * [x] updated `pyproject.toml`

* 231217piu_a invoice header, issue date (&& ATTN pendulum raise error, see `rdinv.py` line #17, ==> MAYBE JUST TRY `Arrow` or standard `datetime`)

* 231216piu_a review, improve & clean code for: `xl_invoices/config_settings.py`, `xl_invoices/rdinv.py`

* 231215piu_b FIXED configs loaded from config_settings: `rdinv` module load (init) all constants as global variables (because they are subject to change / "improve" values as reading Excel file, for example `DEFAULT_CURRENCY`)

* 231215piu_a changed dir name **`xl_invoice_modules/`** to `xl_invoices` or classic `xl2roefact`  as this will be the package name. This is a Python official RECOMMENDATION not a constraint

* 231214piu_a made xl2roefact Python standard package (moved `xl2roefact` modules to a dedicated directory (`xl_invoice_modules/`) with intention to publish package)






### 0.1.13.dev invoice currency (231213 h07:00)

* 231213piu_b build packages for:
    * [x] application deployment package ==> `dist/0.1.13-xl2roefact-0.1-win64.msi`
    * [x] cleaned, tested, created packages (saved to ==> `.../880-RLSE/880.90-RLSE Source Code Archives`)
* 231213piu_a get invoice header - invoice currency






### 0.1.12.dev invoice number (231212 07:30)

* 231212piu_b write canonical form (as @invoice lines, see line ~122) ==> `invoice["Invoice"]["cbc_ID"]` and released `0.1.12-xl2roefact-0.1-win64.msi`

* 231212piu_a `rdinv.rdinv()` invoice header, invoice number as: `{"value": ..., "location": (row..., col...)}`

* 231211piu_b `rdinv.rdinv()` create a function special to get "one key Excel values", like invoice number or invoice issue date.  Signature:
    - `pattern_to_search_for: list[str]` - for inv number will pass the `PATTERN_FOR_INVOICE_NUMBER_LABEL`
    - `area_to_scan: list[start_cell, end_cell]` - for inv number will pass `(invoice_header_area["start_cell"], invoice_header_area["end_cell"])`
    - targeted_tye: type - what type expect (will try to convert to, if cannot will return str)

* 231211piu_a updated `config_settings.py` ref how to find it: string labels to search, direction to search effective info starting from label

* 231210piu_a localized and marked areas for invoice header (`invoice_header_area`) & invoice footer (`invoice_footer_area`) ==> dicts for header and footer with structure `{ start_cell = (row, col), end_cell = (row, col) }`






### 0.1.11.dev (231209 h08:00)

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











# Archived CHANGELOGs

* [0.1.10.dev command interface improved, `msi` package building, invoice template & updated documentation](./changelog_history/CHANGELOG-0.1.10.dev.md)
* [0.1.9.dev `xl2roefact.RDINV` running executable and distribution kit](./changelog_history/CHANGELOG-0.1.9.dev.md)
* [0.1.8.dev improved application structure and first executable release](./changelog_history/CHANGELOG-0.1.8.dev.md)
* [0.1.7.dev `xl2roefact.RDINV` invoice items & metadata + *OPEN ISSUES*](./changelog_history/CHANGELOG-0.1.7.dev.md)
* [0.1.6.dev commercial agreement OPTIONS document](changelog_history/CHANGELOG-0.1.6.dev.md)
* [0.1.5.dev init component *xl2roefact* for CLI application](./changelog_history/CHANGELOG-0.1.5.dev.md)
* [0.1.4.dev Create system backbone structure](./changelog_history/CHANGELOG-0.1.4.dev.md)
* [0.1.3.dev Enhancing `payments_validation_board` technical proposal](./changelog_history/CHANGELOG-0.1.3.dev.md)
* [0.1.2.dev Enhancing `APItoROefact` technical proposal](./changelog_history/CHANGELOG-0.1.2.dev.md)
* [0.1.1.dev Elaborating technical proposal](./changelog_history/CHANGELOG-0.1.1.dev.md)
* [0.1.0.dev System raw backbone](./changelog_history/CHANGELOG-0.1.0.dev.md)







# [Release Notes](RELNOTE.md) #TODO this file should be created

* wip... [not_yet_created... 0.1](./changelog_history/...)
