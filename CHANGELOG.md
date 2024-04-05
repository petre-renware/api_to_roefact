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

### `0.5.4` invoice supplier from owner master data (#TODO: ... in progress...)

* tbd.Must... this release should go to `master` branch being pure release
* tbd... update all `/versions.yml`

* wip... `owner-dbs-file` get OWNER EXTERNAL DATA feature:
    * [x] 1. create `data/owner.yml` structure to exactly what is needed for actual JSON "Invoice..." key
    * [x] 2. created a skeleton for `hier_get_data_file()` module, update its docstring and generate DLD documentation
    * [x] 3. set a new flag for `xl2json` command for getting owner from ext data-file: `--owner -o [FILE]` where `FILE` being defaulted to `./owner.yml` or hierarchy to `data/owner.yml`
    * [x] 4. app_cli.py chk if file is ok and sent it as correct Path if, else raise an err msg and continue from Excel
    * [x] 5. code. Get owner data by using function `hier_get_data_file()`
    * [x] 6. update `owner.yml` file and add bank information
    * [x] 7. code. Get owner bank information from external data file
    * [x] 8. build xl2roefact DLD documentation
    * [x] 9.. code. Review "place where called for OWNER info", clean, update and close code
    * [x] 10. make template for owner data file (`owner_datafile_tmeplate.yml`) and prep it with built-in documentation hints
    * [ ] ... 11. add xl2roefact README doc with section "Utilizare nomenclator de furnizori sau proprietari"
    * [ ] ... prep release `0.5.4`
    * [ ] ... build site and publish as site version `0.5.4.dev0` (temporary value)

* `hier-get-data-file` func to select hierarchical a file from `./` or `data/` (in libutils module):
    * [x] 1. create skeleton `hier_get_data_file(file_name: str) -> Path` in `xl2roefact.libutils` module
    * [x] 2. code function to solve actual functional case from `xl2roefact.config_settings` module
    * [x] 3. update `xl2roefact.config_settings` module to use the new function















# Archived CHANGELOGs


<details markdown="1"><summary markdown="1">
## 0.5 version
</summary>

<!--* [...v_xxx...](./changelog_history/CHANGELOG-xxx.md) -->
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


