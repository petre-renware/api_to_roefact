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



## 0.6 finalize JSON model to contain all RO eFact XML mandatory taga

* tbd... next main job of release
* tbd... prep release upd DLdoc & HLdoc
* tbd... prep release set all versions


### `0.6rc1` invoice type JSON-XML tag

* ... build package version `0.6rc1`
* ... `app-readme-doc` check & update xl2roefact `README.md`:
    * [ ] ... functionalities in this release (JSON schema update)
    * [ ] ... write about invoice type ref `cbc_InvoiceTypeCode`
    * [ ] ... more sections "For developers" ref how manage some settings if introduce `sys_config.py` feature (different of `app_config`)
    * [x] `site-0.6.dev1` restructured whole design presentation for a better view of its architecture: updated from a pure technical view to end-user technical view
    * [x] `240413_01` updated "API Reference" bullet link (from begging of doc) to point directly to published site as intended for `PyPi` availability in project description
* ... delete `xl2roefact/tests...` specs / helper file
* ... test and clean code
* ... `InvoiceTypeCode-param` make a choose application  parameter.
  Values to be taken from `sys_settings` module, object `InvoiceType`
* ... ... ...


### `0.6rc0` system database and parameters 

* `0.6rc0+240420` build and publish release:
    1. update versions for `xl2roefact` and `invoicetoroefact`
    2. build xl2roefact documentation
    4. wheel deliverables build & PyPi publish
    5. ... update `downloads.md`
    6. ... site build & publish
* `sys_settings-invoice-type` populated "system database" with allowed invoice types
    * created `InvoiceTypes` dictionary with allowed invoice types
    * created `InvoiceTypesEnum` as Enum to be used by CLI app parameter (dinamically generated from previous data object)
* `sys_settings-module` created `xl2roefact/sys_settings.py` component dedicated to system settings (ie, not user configurable but only developers; is intended that later versions to use also a database for)
* `cbc_TaxPointDate` will be set to 25 of next month from invoice issued month
* `cbc_DueDate` search `invoice_header_area` ref `PATTERN_FOR_DUE_DATE` pattern. Use found data if not None or default it to `invoice_header_area["issued_date"]["value"] + DUE_DATE_DAYS` if None found
* `PATTERN_FOR_DUE_DATE` update `config_settings.py` & `app_settings.yml`, create `PATTERN_FOR_DUE_DATE = ["scad", "due da", "date due"]` 
* `inv-issdate-todate` upd `rdinv` for final json dict convert & local save invoice issued date in `datetime` format to--> `tmp_reusable_items["invoice_issdate_asdate"]`
* `cac_Delivery` set as invoice issued date
* `cac_PaymentMeans` will be set to `1` supposing is unknown at invoicing issuing date
* `DEFAULT_DUE_DATE_DAYS` new app config parameter with default value 30 days
* `cbc_Note` set to "proccesed @`{date_time_now}` with xl2roefact". Latter this field will be updated with text ref loading to RO-eFact data-time
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


