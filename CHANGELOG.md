<small>**RENware Software Systems**</small>

**INVOICEtoROeFact** Project

[TOC]


# CHANGELOG

- For version code structure meaning see [SDEVEN methodology document](http://sdeven.renware.eu)
- `<PROJECT ROOT>/doc_src/` is the default starting location in a file path (if not clear from context) (**ATTN** - in production environment is `docs/`)
- `<WEB_ROOT>/` is the HTTP server root directory, as default `docs/` and supposed if no other parent is specified


<!-- #TODO #NOTE ...
====[ General PLAN ]====

* ---[ general planning board ]---:
    * -#NOTE link Swagger servicii web: `https://mfinante.gov.ro/web/efactura/informatii-tehnice`
    * -#NOTE link specif API incarcare fact: `https://mfinante.gov.ro/static/10/eFactura/upload.html#/EFacturaUpload/handleRequest`

* ---[ FUTURE NEW APP COMMANDS ]---:
    * `config` - set `config_settings.py` variables (make it INTERACTIVELY using `Rich prompt`)
    * `xl2json` - crt_wip... (last upd @ 240219piu_a)
    * `json2xml` - see module WRXML,
    * `json2pdf` - new module. tbd..,
    * `xml2roefact` - see module LDXML
    * chk for other commands from doc `https://invoicetoroefact.renware.eu/commercial_agreement/110-SRE-api_to_roefact_requirements.html#componenta-xl2roefact`

* ---[ Plan for `rdinv` module ]---:
        * [ ] ...wip in 0.4... invoice supplier (`<cac:AccountingSupplierParty>`)
-->




## 0.5

### 0.5.3rc0 invoice supplier (#TODO: ... in progress...)

* tbd... update all `/versions.yml`

* tbd... get OWNER EXTERNAL DATA feature code here, but can RELEASE A `0.5.3rc0` VERSION BEFORE and `0.5.3rc1` AFTER DO THAT


* ... `240327piu01` build & publish wheel on PyPi
    * [x] 1. update xl2roefact README add link "API Reference" to DLD doc (to be accesible from PyPi)
    * [x] 2. update xl2roefact `setup.py` and include documentation directory (`doc/`) in WHEEL & DIST packages
    * [x] 3. `README_xl2roefact_library.md` review & clean of useless content ("rdinv module logic", "Working directories") and refer it in main xl2roefact README before "Referinta API" bullet link
    * [ ] ... review xl2roefact README, installation section
    * [ ] ... review xl2roefact README, tutorial
    * [ ] ... update JSON model ref new supplier section
    * [ ] ... update `xl2roefact/__version__.py`
    * [ ] ...

* `240325piu-use-new-function` import new function `get_partner_data()` and use it in `rdinv.py` module
    * [x] 1. include function `get_partner_data()` in `rdinv.py` and test for simple compilation errors => result: PASS
    * [x] 2. rebuild DLD documentation
    * [x] 3. use in code to replace actual existing CUSTOMER data retrieve. Test for no change vs previous functionality => result: PASS
    * [x] 4. make a new call for SUPPLIER data. Test for raw getting data in "...excel...original...data" key => PASS
    * [x] 5. chk new get data and make needed adjustments
    * [x] 6. update `rdinv.py` to create all supplier final constructs (like those for customer after getting data). Test result: PASS
    * [x] 7. update XML-JSON map using code refactored @ `rdinv.py lines 287-309`
    * [x] 8. clean code of FIXME and other work comments and built DLD doc
* `240323piu-suppl-configs` rollout supplier configuration parameters from `.../xl2roefact/___wk_cust_area_function.py`:
    * [x] 1. update `config_settings.py` with their definition. Tested PASS
    * [x] 2. update `data/app_settings.yml` with their definition. Tested PASS. Cleaned file `.../xl2roefact/___wk_cust_area_function.py` to make easier its transport to `rdinv.py`
    * [x] update `rdinv.py` with their import
    * [x] test `xl2roefact`: automation on `test-xl2roefact` branch
    * [x] build DLD (`pdm run build_doc`)
* `upd-shebang` update all xl2roefact modules, drop shebang statement
* `240320piu-invsuppl` code for `INV.SUPP`... `xl2roefact` invoice supplier (`<cac:AccountingSupplierParty>`)
    * [x] 1. extracted code to generalize in `.../xl2roefact/___wk_cust_area_function.py` to "engineer it"
    * [x] 2. wrap code in new function `get_partner_data()`, set its first param `partner_type` for desired function operation and protect function against unknown values
    * [x] 3. 1st raw refactoring: constants dedicated to CUSTOMER adjusted as UNIFyed...PARTNER... and set for customer or supplier depending on partner_type
    * [x] 4. 2nd raw refactoring: `customer_area` string. This is a keyword, so it is subject to unification based on partner_type resulting `partner_area` variable used as keyword instead of hard code "customer_area"
    * [x] 5. mark & comment in `rdinv.py` place where call this function, start / end of code that should be dropped by using this function (rdinv.py start line 229, end line 367, marker #FIXME.UNIF.PARTNER.DATA)
    * [x] 6. updated `invoice_header_area` with `param_invoice_header_area` and set las as function parameter
    * [x] 7. updated `invoice_customer_info` with `invoice_partner_info`
    * [x] 8. replace word "customer" with "partner" keeping original case
    * [x] 9. set new parameter `wks` as replacement of `ws` variable (supposed by original code as already existing). Type of this parameter is `pylightxl.Worksheet`.


### `0.5.2.dev2` release xl2roefact.`0.4.1.dev1` fix sEXE bug from `0.4.1.dev0` version:

* [x] 1. update `config_settings.py` module to load app cfg from external file only when not sEXE frozen app (`getattr(sys, 'frozen', False) == True`)
* [x] 2. update xl2roefact version to `0.4.1.dev1` to genrate only sEXE deliverable
* [x] 3. test python code. Result: **PASS**
* [x] 4. generate sEXE
* [x] 5. test `pdm run xl2roefact settings`. Result: **PASS**
* [x] 6. clean and make code "production like"
* [x] 7. update INVOICEtoROefact project `versions.yml`:
    * xl2roefact = 0.4.1.dev1
    * INVOICEtoROefact = 0.5.2.dev2
* [x] 8. build xl2roefact wheel and DLD doc
* [x] 9. publish `0.4.1.dev1` on PyPi
* [x] 10. build all deliverables
* [x] 11. update downloads.md ref all deliverables
* build site & publish


### `0.5.1.dev1` site readability improvements:

* [x] 1. main project README drop `TOC` statement
* [x] 2. update `nav -> Help -> CHANGELOG sistem`, change to "Istoric log sistem"
* [x] 3. update downloads.md doc, mark as "known bug DO NOT USE" entry:
    - section: "Aplicatia xl2roefact linie comanda executabil portabil (win64-exe)"
    - entry: "0.4.1.dev0 xl2roefact include a data directory in package"
* update *INVOICEtoROefact* system ver to `0.5.1.dev1`
* build site & publish














<!--#TODO: subject to archive. When do it see if add to archived CHANGELOG the "antet" section ref components version -->
#FIXME --- drop me after finish 
### `0.4.1.dev0` xl2roefact include a data directory in package for various data files "built-in" package (240318 h09:00)

* `240318piu-yaml4sys-all-vers` update `mkdocs.yml` use `INHERIT: ./versions.yml` option to inherit versions exactly to have `extra` section like actual one but in this external file.
* `240318piu-app-glob-cfg` update xl2roefact README, app configuration section ref how make a "global config file" different than default app configuration
* `240317piu01` update downloads.md:
    * [x] 1. include a template for `app_settings.yml` => Created dedicated section which can be referred as `.../downloads.md#sablon-fisier-configurare-a-aplicatiei-xl2roefact`
    * [x] 1.a fixed `0.4.0.dev2` MSI & EXE deliverables file names (missing path number)
    * [x] 2. refer it in xl2roefact README
    * [x] 3. include `0.4.1.dev` download;
        * WHEEL & DIST references
        * standalone EXE reference
        * MSI reference
* `2403piu-config-code` update `config_settings.py` module to upload data from `.../data/app_settings.yml` file. Specs:
    * [x] 1. update app version to `0.4.1.dev0`. Make a test what `normalized_version()` returns (run xl2roefact --version)
    * [x] 2. update key `README_rules` from `app_settings.yml`, set it to point to markdown file containing rules list (`xl2roefact/xl2roefact/data/README_app_config_rules.md`)
    * INFO-NOTE: after YAML import data will be dict with all actual code variables as keywords
    * [x] 3. gross-raw code in `config.settings.py` for both below NOTES
        * INFO-NOTE: order to search and load for `app_config.yml`:
            * (1) crt directory (with `cwd`) with `Path(Path.cwd(), "data/app_settings.yml")`
            * (2) package directory and file with `Path(os.path.dirname(__file__), "data/app_settings.yml")`
            * (3) settings from `config_settings.py`
        * INFO-NOTE: methods of updates variables:
            * (1) using `locals().update(YAML_dict)`
            * (2) using `exec(YAML_dict["key")` by looping YAML resulted dictionary
        * regardless of method check the propagation running `xl2roefact settings` which is a demo of using values external to config_settings module
    * [x] 4. apply reading order
    * [x] 5. clean code & test YAML settings files from `xl2roefact/`
    * [x] 6. if read YAML was got some values then set as `local()` variables (not dictionary)
    * [x] 7. updated `xl2roefact/setup.py` to include `data/app_settings.yml` file
    * [x] build all: upd version (2 version files + mkdocs.yml) & pdm run build_all
* `2403piu-app-data-dir` actions:
    * [x] 1.a build directory with a TOML file for setting parameters (used by `config_settings` module)
    * [x] 2 update `pyproject.toml` to include in package non python data files from `xl2roefact/data/` directory
    * [x] 2.a test pdm building wheel ref brute errors = __PASS__ =: package created ok and contains `data/*` with exact flies that exists in this directory at package development phase
    * [x] 3. add in `.../xl2roefact/data/` file `owner_data.json` with owner data to be used as supplier info for future option `--load-from-owner-file`
    * [x] 4. fixed bug xl2roefact CLI app ref command `about` printing `__version__.__doc__` addressing
    * [x] 5. updated `.../data/app_settings.yml` with actual existing config data. Not usable as is, need refining and clarify how to indicate data types to app users (actually indicated as Python type hints)
#FIXME --- drop me after finish 





# Archived CHANGELOGs

<details markdown="1"><summary markdown="1">
## 0.4 version
</summary>

* [`0.4.1.dev0` xl2roefact include a data directory in package for various data files "built-in" package](
./changelog_history/CHANGELOG-0.4.1.dev0.md
)

* [`0.4.0.dev2` externalize recommended rules for updating app setting rules](./changelog_history/CHANGELOG-0.4.0.dev2.md)
</details>




<details markdown="1"><summary markdown="1">
## 0.3 version
</summary>

* [`0.3.2b0` single EXE version](./changelog_history/CHANGELOG-0.3.2b0.md)
* [`0.3.1b1` fixed bug JSON->["Invoice"]["cac_InvoiceLine"] list[list]](./changelog_history/CHANGELOG-0.3.1b1.md)
* [`0.3.1b`  promote v0.3.0b0 deliverables: WHEEL, TRA.GZ, MSI to `0.3.1b`](./changelog_history/CHANGELOG-0.3.1b.md)
* [`0.3.0b` xl2roefact invoice taxes summary](./changelog_history/CHANGELOG-0.3.0b.md)
</details>




<details markdown="1"><summary markdown="1">
## 0.2 version
</summary>

* [`0.2.2.dev` project development environment improvements](./changelog_history/CHANGELOG-0.2.2.dev.md)
* [`0.2.1b` invoice grand totals](./changelog_history/CHANGELOG-0.2.1b.md)
* [`0.2.0b` xl2roefact invoice customer info-optional items (bank, email, reg-com, phone)](./changelog_history/CHANGELOG-0.2.0b.md)
</details>




<details markdown="1"><summary markdown="1">
## 0.1 version
</summary>

* [`0.1.22b` xl2roefact application interface improvements](./changelog_history/CHANGELOG-0.1.22b.md)
* [`0.1.21.post3` cleaned system documentation and site](./changelog_history/CHANGELOG-0.1.21.post3.md)
* [`0.1.21.post2` xl2roefact app detailed section with commands & options "--help" like](./changelog_history/CHANGELOG-0.1.21.post2.md)
* [`0.1.21.post1` fixed missing links in site root index page](./changelog_history/CHANGELOG-0.1.21.post1.md)
* [`0.1.21` rollout news in system portal invoicetoroefact.renware.eu](./changelog_history/CHANGELOG-0.1.21.md)
* [`0.1.20.dev` invoice customer address](./changelog_history/CHANGELOG-0.1.20.dev.md)
* [`0.1.19.dev` invoice customer and partial invoice total values calculations](./changelog_history/CHANGELOG-0.1.19.dev.md)
* [`0.1.18.dev` invoice customer CUI partial invoice total values calculations](./changelog_history/CHANGELOG-0.1.18.dev.md)
* [`0.1.17.dev` fixed all application & package running standard ways](./changelog_history/CHANGELOG-0.1.17.dev.md)
* [`0.1.16.dev` improving Excel kv-data search with "IN-LABEL" method](./changelog_history/CHANGELOG-0.1.16.dev.md)
* [`0.1.15` updated solution portal `http://invoicetoroefact.renware.eu/`](./changelog_history/CHANGELOG-0.1.15.md)
* [`0.1.14.dev` invoice issue date](./changelog_history/CHANGELOG-0.1.14.dev.md)
* [`0.1.13.dev` invoice currency](./changelog_history/CHANGELOG-0.1.13.dev.md)
* [`0.1.12.dev` invoice number](./changelog_history/CHANGELOG-0.1.12.dev.md)
* [`0.1.11.dev` packaging improvements for app & xl2roefact package](./changelog_history/CHANGELOG-0.1.11.dev.md)
* [`0.1.10.dev` command interface improved, `msi` package building, invoice template & updated documentation](./changelog_history/CHANGELOG-0.1.10.dev.md)
* [`0.1.9.dev` `xl2roefact.RDINV` running executable and distribution kit](./changelog_history/CHANGELOG-0.1.9.dev.md)
* [`0.1.8.dev` improved application structure and first executable release](./changelog_history/CHANGELOG-0.1.8.dev.md)
* [`0.1.7.dev` `xl2roefact.RDINV` invoice items & metadata + *OPEN ISSUES*](./changelog_history/CHANGELOG-0.1.7.dev.md)
* [`0.1.6.dev` commercial agreement OPTIONS document](changelog_history/CHANGELOG-0.1.6.dev.md)
* [`0.1.5.dev` init component *xl2roefact* for CLI application](./changelog_history/CHANGELOG-0.1.5.dev.md)
* [`0.1.4.dev` Create system backbone structure](./changelog_history/CHANGELOG-0.1.4.dev.md)
* [`0.1.3.dev` Enhancing `payments_validation_board` technical proposal](./changelog_history/CHANGELOG-0.1.3.dev.md)
* [`0.1.2.dev` Enhancing `APItoROefact` technical proposal](./changelog_history/CHANGELOG-0.1.2.dev.md)
* [`0.1.1.dev` Elaborating technical proposal](./changelog_history/CHANGELOG-0.1.1.dev.md)
* [`0.1.0.dev` System raw backbone](./changelog_history/CHANGELOG-0.1.0.dev.md)
</details>


