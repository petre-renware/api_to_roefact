<small>**RENware Software Systems**</small>

**INVOICEtoROefact** Project

[TOC]


# CHANGELOG

- For version code structure meaning see SDEVEN methodology document
- with _(F)_ are marked those changes that are features in order to be copied in a RELNOTE file and with _(B)_ bug fixes from versions released
- publishing is made under `publishing` branch
- `<PROJECT ROOT>/doc_src/` is the default starting location in a file path (if not clear from context) (**ATTN** - in production environment is `docs/`)
- `<WEB_ROOT>/` is the HTTP server root directory, as default `docs/` and supposed if no other parent is specified



## 0.1 (-#NOTE_wip...)

```
    - ---[ #TODO general planning board ]---------------------------
    * ai un exemplu complet si complet agnostic (trimis Gigi) de factura format XML si PDF tiparit ca sa faci: (1) incarcare XML (2) geenrare PDF (3) compararea variantelor si identificarea schemei XSD + document specificatii ANAF ref sistemul E-Factura (PDF trimis Liviu)
    * -#NOTE link Swagger servicii web: `https://mfinante.gov.ro/web/efactura/informatii-tehnice`
    * -#NOTE link specif API incarcare fact: `https://mfinante.gov.ro/static/10/eFactura/upload.html#/EFacturaUpload/handleRequest`

    - ---[ #TODO short planning board ]---------------------------
    * left OPEN ISSUES on: `0.1.7` release (and drop them when fixed)
        * [ ] _file `xl2roefact\invoice_files/_PLAN_model_test_factura_generat_anaf.xml`, line 114:_ `<cbc:ID>S</cbc:ID> #FIXME clarify.me_ pare a fi TIPUL PRODUSULUI: (S)erviciu sau ??? (P)rodus sau ???`
    -
    * ... FUTURE NEW APP COMMANDS :
        * `config` - set `config_settings.py` variables (make it INTERACTIVELY using `Rich prompt`)
        * `xl2json` - crt_wip... (last upd @ 240123)
        * `json2xml` - see module WRXML,
        * `json2pdf` - new tbd..,
        * `xml2roefact` - see mpdule LDXML
        * chk for other commands from doc `https://apitoroefact.renware.eu/commercial_agreement/110-SRE-api_to_roefact_requirements.html#componenta-xl2roefact`
        * PACKAGE SOLUTION:
            * [ ] publish `xl2roefact` package --> read `TODO_packaging.md`
    -
    * -#NOTE_PLAN `rdinv` module:
        * invoice header
            * [ ] wip... invoice header - customer bank, RegCom, email, tel, ...
            * [ ] invoice header - supplier (`<cac:AccountingSupplierParty>`)
            * [ ] invoice grand totals (there was left a comment ref whole XML structure in rdinv(), line # ~ where build & write "Invoice" key)
    -------------------------------------------------------------------------------------------------
```




### 0.1.22.dev invoice customer address optional items (email, reg-com, phone) (#NOTE nxt... ...yymmdd hh:mm...)

* TODO:_ASAP after 0.1.19 consider **0.1.0** where to update main portal doc and change:
    - all `APItoROefact` ==>  **`xl2roefact`** cu inteles de **`Excel invoices and RO eFact`**
    - portal main navigation: link to GitHub Issues refined for 2 entries: *bugs* & *suport si documentatie utilizare*

* tbd... WHEN RELEASE UPDATE make a full chk / review for FIXME & run `pdm build_all`

* tbd.optional... [piu_240126] left in `setup.py` comments & example ref how to pre-set MSI build meta information / parameters (obj: default target dir where install, path registration, ...)

* tbd... invoice customer search for other keys: "reg com", "bank / IBAN / cont", "tel", "email" (start in `rdinv()` w./line 179 & then 331)

* wip... last item used 240203piu_a








### 0.1.21.post1 fixed missing links in site root index page (240203 10h:30)

* 240203piu_a fixed links in `/README.md` for: `xl2roefact PyPi` entry






### 0.1.21 rollout news in system portal invoicetoroefact.renware.eu (240203 h09:00)

* 240201piu_a reorganized `xl2roefact*` components by disseminating the installable application, which is something available "as is now" just for Windows operating system. For Linux there is no difference between command line application and Python package *from an end user point of view*.
* 240131piu_a `xl2roefact/doc/810.05a-xl2roefact_component.md` clean & transform to "first entry to `xl2roefactPyPi`"
* 240131piu_a updated `mkdocs.yml`: cleaned navigation, created version variables, updated default site build directory to `docs/`, cleared excluded directories entry
* 240130piu_b reviewed all changes, update site PDF generator file (mvd `print_page.md` to root) location, fixed navigation. PUBLISHED for `xl2roefact` component
* 240130piu_a reviewed `xl2roefact` README: cleaned, translated 2 RO, structured to "end user needs"
* 240129piu_d updated `xl2roefact` to have "Descrierea detliata" link in `810.05a-system_components.md`. Prepared component to be published: mkdocs.yml navigation & main site README index
* 240129piu_c updated all site pages to contain `<small>**RENware Software Systems**</small>` & `[TOC]` after title
* 240129piu_b cleanup project docs, requirements, fresh install ==> published site as is at this point (invoice template finished)
* 240129piu_a updated `xl2roefact/README.md` with section for assets download
* 240128piu_e formal versioning `invoice template` component
* 240128piu_d updated & closed component `invoice template`. Referred in:
    * `doc_src/810-DSGN/810.05a-system_components.md`
    * portal first page
    * navigation in `mkdocs.yml`
* 240128piu_c moved `xl2roefact/excel_invoice_template/` directory to root as being distinct component, review it and closed to be published
* 240128piu_b revised, updated and closed crt version of `excel_invoice_template/README.md`
* 240128piu_a updated `xl2roefact/README.md` & `excel_invoice_template/README.md` files, cleared modularization & structure presented in system public site
* 240127piu_d Unify main project `/READMEmd` with `doc_src/index.md`:
    * make the same INDEX just in the project root == index / README of whole project
    * keep from actual project README.md the section ref project identification and move it to end of file as last section
* 240127piu_c created `/index.html` to redirect to "real" system index (`doc_src/index.md`) and prevent usage of project `README.md` file instead
* 240128piu_c checked work `240127piu_a`, `240127piu_b`, updated `about.md` and navigation with ref to sys structure (`.../810.05a-system_components.md`)
* 240127piu_b update system components and their classification (in `.../810-DSGN/810.05a-system_components.md`)
* 240127piu_a updated `810-DSGN/810.05a-system_components.md`, defined a classification usable to quickly find out *who-does-what*
* 240125piu_a updated `mkdocs.yml` by including `mkdocs-same-dir` plug-in






### 0.1.20.dev invoice customer address (240123 h10:00)

* 240123piu_b make a full chk / review for FIXME & run `pdm build_all`

* 240123piu_a `def_inv_dir` issue ref Excel invoices default get directory, see comments in `app_cli.py` function `xl2json(...)`

* 240121piu_a updated `config_settings.py` & `rdinv.py` with constants: `PATTERN_FOR_PARTNER_REGCOM`, `PATTERN_FOR_PARTNER_IBAN`, `PATTERN_FOR_PARTNER_TEL`, `PATTERN_FOR_PARTNER_EMAIL`, `PATTERN_FOR_PARTNER_BANK`

* @CANCELED 240118_admin02 generalize a function `get_partner_info(partner_type: str "customer" | "supplier")` to get partner info with partner type as being parameter

* 240118piu_a reviewed and cleaned code: `rdinv.rdinv()`, `config_settings`, `excel_invoice_template/invoice_template_CU_tva.xlsx` (according to updates in testing used invoice)

* 240113piu_a to find `cac:PostalAddress` and write to:
    * [x] 1. right set position of key `"cac_PostalAddress"` in basic structure (invoice_header_area)
    * [x] 2a. find excel area ref customer address (...invoice_header_area...)
    * [x] 2b. disseminate & save excel original area (...invoice_header_area...)
    * [x] 3. get & set `["Invoice"]["cac_PostalAddress"]` and all is subsequent keys
    * [x] 4. update XML - JSON map for item "under" `cac_PostalAddress`
    * [x] 5. defined and included for use `DEFAULT_SUPPLIER_COUNTRY` and `DEFAULT_CUSTOMER_COUNTRY` both for "RO". Detailed desc and usage in `config_settings.py` & `rdinv.rdinv(...)`
    * [x] 6. updated invoice template for country explicit field

* 240116_admin_01 upd __version__ for 0.1.20






### 0.1.19.dev invoice customer and partial invoice total values calculations (240116 h06:00)

* 2401_xl2roefact_doc_01 `xl2roefact` update technical documentation, file `xl2roefact/doc/810.05a-xl2roefact_component.md`

* 240112piu_b 95% clean code `rdinv()` from customer area identification, from line 204 (kept a DBG print just for area identification (useful for next task ref the same opers but for Supplier))

* 240112piu_a module `app_cli.py`, created `called_when_no_command(...)` function called when no command is invoked and to provide only application version (for external users to test it!)

* 240110piu_c `xl2json` `about` command to get version & "nice" LOGO from `xl2roefact/__version__.py`, vars `__version__` & `__doc__`

* 240110piu_b `xl2roefact/setup.py`ref get app version from file when build EXE/MSI test for `__version__` is correctly get and release

* 240110piu.a reviewed & updated `xl2roefact` package `README.md` + `xl2roefact/__version__.py` with an app logo and for text mistyping bugs

* 240108piu_c changed `pyproject.toml` for auto update package version from file `xl2roefact/__version__.py` (see also opiss 240108piu_b)

* 240108piu_b created `xl2roefact/__version__` file that contains variable `__version__` with INTENTION to use in `pyproject.toml` for app version key (in a future issue)

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












# Archived CHANGELOGs

* [0.1.14.dev invoice issue date](./changelog_history/CHANGELOG-0.1.14.dev.md)
* [0.1.13.dev invoice currency](./changelog_history/CHANGELOG-0.1.13.dev.md)
* [0.1.12.dev invoice number](./changelog_history/CHANGELOG-0.1.12.dev.md)
* [0.1.11.dev packaging improvements for app & xl2roefact package](./changelog_history/CHANGELOG-0.1.11.dev.md)
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
