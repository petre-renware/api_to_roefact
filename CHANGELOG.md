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
    * `xl2json` - closed
    * `json2xml` - see module WRXML,
    * `json2pdf` - new module. tbd..,
    * `xml2roefact` - see module LDXML
    * chk for other commands from doc `https://invoicetoroefact.renware.eu/commercial_agreement/110-SRE-api_to_roefact_requirements.html#componenta-xl2roefact`
-->



<!--   ## tbd.nxt... `0.10` invoice XML output
* make `json2xml`  -->






## `0.9` init commands layer 2 of functionalities

* tbd... move `xl2json` functionality to `l2_commands.py`
* tbd... move `settings` functionality to `l2_commands.py`
* tbd... update doc `README_xl2roefact_library.md` make a small hierarchical diagram with component layers
* tbd... upd versions to `0.9b0`
* ... `upd-DLD` upd all `xl2json` docstring and generate new DLD doc
* ... `main-code-cls` close `xl2json` method by prep status result before owner file not valid exiting & close all open TODO_FIXME issues
* `main-code-ini` create `commands.py` to accommodate *layer 2 commands functionalities*
* update version to `0.9.dev0`






## `0.8` BUGFIX xl2roefact entry point

* upd xl2roefact dowloads & build site
* make WHEEL deliverables: build, PyPi publish
* created `gitupd_tags.sh` to update all local tags keeping only remote ones & made it execurable
* updated versions
* BUGFIX updated `xl2roefact.setup.py` entry point for `xl2roefact` to correct to `xl2roefact.app_cli...` from `src.app_cli...`






## `0.7` clean xl2roefact package and invoice JSON

* `update downloads` ref 0.7 dlvbs & reorganize it with 1st level. Follow:
    * ref new structure & locations of download docs
    * [x] update master downloads.md ref old versions drop
    * [x] links: add `0.7`
    * [x] remove all links `<= *0.5*`
    * [x] removed all deliverables `<= *0.5*`
* build & publish deliverables + site
* build & publish site with new downloads structure
* `brk-doc_src/downloads.md` letting it as *master* and making specialized download pages in `xl2roedact/doc/package_downloads.md` and `excel_invoice_template/package_downloads.md`:
    * [x] updated new downloads files for existing deliverabkes
    * [x] created directories structure & empty files
* update version & site
* `xl2roefact-refactor`
    * fixed `xl2roefact` command `xl2json` option `-o`, set ver to `.dev`, rebuilt dld doc and site
    * reverted to flat package structure, without src/ directory but only xl2roefact/
    * updated PDM scripts and made package from src/ directory (created __init__.py)
    * refactored xl2roefact source files
* `upd-site` updated sitem left side navigator to better reflect the new features / system architecture
* `fix-site` 0.7rc2 downloads.md, link to "Descarcare sablon de fisier de configurare"

### `0.7rc2` updated console application to run in  silent or vebosed

* updated downloads.md & built site
* review & update DLD doc, build all deliverables and publish on PyPi
* `app_cli.xl2json` updated to write function out at verbose or otherwise (ie, not verbose) just its print messages. Also eliminate the JSON printing when verbose because no more debug necessary at this moment
* `rdinv-silent` updated `rdinv.rdinv()` in order to run "in silent" and to emit all print info in a specified parameter not None, or (if parameter is None or not specified) emmit normally to `stdout` device
* `init-command-layer` made `commands/` as in-package / layer
* upd versions before start work

### `0.7rc1` review & clean `xl2roefact.rdinv` module of TODOs

* 4. publish PyPi, upd downloads.md, site
* 3. build only wheel deliverable because only source library is impacted
* 2. review TODOs, keep only those that are future features and move them to ROADMAP
* 1. upd versions before start work

### `0.7rc0` settings refresh option and app settings reload by request

* update downloads, site
* Published on PyPi (`https://pypi.org/project/xl2roefact/0.7rc0/`)
* updated doc, deliverables
* `config-settings-main-func` update config_settings module to embed init code under a `main()` function which run @ init but can be latter called also
* `240429piu01` update doc `README_xl2roefact_library.md` section "Library components" to reflect the new commands layer. Rebuild site & publish
* fix `invoicetoroefact.renware.eu` site for 0.6 MSI & EXE downloads








## `0.6` invoice type JSON-XML tag

* `upd-dwnlds` update downloads.md. site rebuild & publish
* `pypi-publish` publish on PyPi
* `xl2roefact-build` build all `0.6` deliverables
* `app-readme-doc` check & update xl2roefact `README.md`:
    * [x] example JSON schema update & build + publish site
    * [x] `doc-sys-settings-feat` short note about allowed invoice type (`cbc_InvoiceTypeCode`)
    * [x] `doc-sys-settings-feat` in xl2roefact library doc, ie "Referinta dezvoltare sofrware" (`README_xl2roefact_library.md`) explain how manage system settings using `sys_config.py`
    * [x] `for-dvelopers-section` introduce a new section "Referinta dezvoltare sofrware" to group existing and all new things ref xl2roefact library. Reference to existing `README_xl2roefact_library.md`
    * [x] `site-0.6.dev1` restructured whole design presentation for a better view of its architecture: updated from a pure technical view to end-user technical view
    * [x] `240413_01` updated "API Reference" bullet link (from begging of doc) to point directly to published site as intended for `PyPi` availability in project description
* xl2roefact change version
* `refact-xl2roefact-modules-dirname` refactoring xl2roefact modules directory name to `src/` (old was `xl2roefact/`)
* `InvoiceTypeCode-app-param` make `invoice_type_code` choose-type app parameter
* `InvoiceTypeCode-func-param` make `xl2roefact.rdinv()` parameter `invoice_type_code` parameter with default value `InvoiceTypesEnum.NORMALA`

### `0.6rc0` system database and parameters

* `0.6rc0+240420` build and publish release:
    1. update versions for `xl2roefact` and `invoicetoroefact`
    2. build xl2roefact documentation
    4. wheel deliverables build & PyPi publish
    5. updated `downloads.md`
    6. site build & publish
* `sys_settings-invoice-type` populated "system database" with allowed invoice types
    * created `InvoiceTypes` dictionary with allowed invoice types
    * created `InvoiceTypesEnum` as Enum to be used by CLI app parameter (dynamically generated from previous data object)
* `sys_settings-module` created `xl2roefact/sys_settings.py` component dedicated to system settings (ie, not user configurable but only developers; is intended that later versions to use also a database for)
* `cbc_TaxPointDate` will be set to 25 of next month from invoice issued month
* `cbc_DueDate` search `invoice_header_area` ref `PATTERN_FOR_DUE_DATE` pattern. Use found data if not None or default it to `invoice_header_area["issued_date"]["value"] + DUE_DATE_DAYS` if None found
* `PATTERN_FOR_DUE_DATE` update `config_settings.py` & `app_settings.yml`, create `PATTERN_FOR_DUE_DATE = ["scad", "due da", "date due"]`
* `inv-issdate-todate` upd `rdinv` for final json dict convert & local save invoice issued date in `datetime` format to--> `tmp_reusable_items["invoice_issdate_asdate"]`
* `cac_Delivery` set as invoice issued date
* `cac_PaymentMeans` will be set to `1` supposing is unknown at invoicing issuing date
* `DEFAULT_DUE_DATE_DAYS` new app config parameter with default value 30 days
* `cbc_Note` set to "processed @`{date_time_now}` with xl2roefact". Latter this field will be updated with text ref loading to RO-eFact data-time
* `init-work` set site & xl2roefact versions to `0.6rc1`

### `0.6.dev1` code missing XML tags

* `arch-prev-rlse-chlogs` archive `0.5.4` CHANGELOG
* `xml-json-map` updated `xl2roefact.rdinv` module for XML-JSON map
* `fin-xml-specs` made `xl2roefact/tests/todosXML.md` file with list of XML tags to do and all other specs to complete activity
* `init-work` set site & xl2roefact versions to `0.6.dev1`

### `0.6.dev0` clean xl2roefact & invoicetoroefact projects (...yymmdd hhmm...)

* `240408piu-adm1` cleaning and updating version strings and code
    * rebuild site
    * update xl2roefact/__version.py__
    * update main versions.yml
* `240408piu-adm1`  cleaning and updating environments:
    * updated xl2roefact python requirement, relaxed to `>=3.10`
    * updated site version to `0.6.1dev0` to mark in progress work
    * installed `chromium` on dev server






# Archived CHANGELOGs

<!--* [...v_xxx...](./changelog_history/CHANGELOG-xxx.md) -->

<details markdown="1"><summary markdown="1">
## 0.5 version
</summary>

* [`0.5.4` invoice supplier from owner master data](./changelog_history/CHANGELOG-0.5.4.md)
* [`0.5.3rc1` fix invoice JSON key "cac:Party" naming](./changelog_history/CHANGELOG-0.5.3rc1.md)
* [`0.5.3rc0` invoice supplier from Excel](./changelog_history/CHANGELOG-0.5.3rc0.md)
* [`0.5.2.dev2` release xl2roefact.`0.4.1.dev1` fix sEXE bug from `0.4.1.dev0` version](./changelog_history/CHANGELOG-0.5.2.dev2.md)
* [`0.5.1.dev1` site readability improvements](./changelog_history/CHANGELOG-0.5.1.dev1.md)
</details>




<details markdown="1"><summary markdown="1">
## 0.4 version
</summary>

* [`0.4.1.dev0` xl2roefact include a data directory in package for various data files "built-in" package](./changelog_history/CHANGELOG-0.4.1.dev0.md)
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


