<small>**RENware Software Systems**</small>

**INVOICEtoROefact** Project

[TOC]


# CHANGELOG 0.1.14.dev








_agreement/110-SRE-api_to_roefact_requirements.html#componenta-xl2roefact`
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






