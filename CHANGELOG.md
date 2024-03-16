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



<!-- NOTE: set to 0.5... because invoice supplier is a functional change ...
## 0.5 

### TODO:plan 0.5rc0 invoice supplier  (...date_here...)

* tbd.Must... @RELEASE update version files & [follow `/RELEASE-QA_checklist.md`](./RELEASE-QA_checklist.md)

* tbd.Could... define `xl2roefact` entry points and/or scripts. comments in `xl2roefact/setup.py` ref exec scripts with installed package

* tbd.Should... [piu @_240126] left in `xl2roefact/setup.py` comments & example ref how to _`pre-set MSI build meta information`_ / parameters (obj: default target dir where install, path registration, icon, ...)

* tbd.Must...code: `INV.SUPP`... `xl2roefact` invoice supplier (`<cac:AccountingSupplierParty>`)
    * start with search where produce `"supplier_area": "...future..."` (JSON extract) or "FIXME: INV.SUPP"
    * ... idea is to reuse code for customer area as much as possible

-->





## 0.4 ...wip

### wip... `0.4.1.dev0` xl2roefact include a data directory in package for various data files "built-in" package

* ...tbd... update downloads and include a template for `app_settings.yml` and specify in xl2roefact README
* ...tbd... check if everything is ok when make EXE & MSI variants, meaning defaults the right data and process of Excel files is correct w/o errors
* ...tbd.. build a new wheel package (#NOTE: ATTN TO VERSION)
* ...wip... `2403piu-config-code` update `config_settings.py` module to upload data from `.../data/app_settings.yml` file. Specs:
    * [ ] 1. update app version to `0.4.1.dev3`. Make a test what `normalized_version()` returns (run xl2roefact --version)
    * [ ] 2. drop key `README_rules` from `app_settings.yml`, ref to rules
    * INFO-NOTE: after YAML import data will be dict with all actual code variables as keywords
    * [ ] 3. keep all existing variables and read YAML file if exists and replace their content (avoid defaulting errors when file is not defined)
    * INFO-NOTE: order to search and load for `app_config.yml`:
        * (1) crt directory (with `cwd`) with `Path(Path.cwd(), "data/app_settings.yml")`
        * (2) package directory and file with `Path(os.path.dirname(__file__), "data/app_settings.yml")`
        * (3) settings from `config_settings.py`
* `2403piu-app-data-dir` actions:
    * [x] 1.a build directory with a TOML file for setting parameters (used by `config_settings` module)
    * [x] 2 update `pyproject.toml` to include in package non python data files from `xl2roefact/data/` directory
    * [x] 2.a test pdm building wheel ref brute errors = __PASS__ =: package created ok and contains `data/*` with exact flies that exists in this directory at package development phase
    * [x] 3. add in `.../xl2roefact/data/` file `owner_data.json` with owner data to be used as supplier info for future option `--load-from-owner-file`
    * [x] 4. fixed bug xl2roefact CLI app ref command `about` printing `__version__.__doc__` addressing
    * [x] 5. updated `.../data/app_settings.yml` with actual existing config data. Not usable as is, need refining and clarify how to indicate data types to app users (actually indicated as Python type hints)






-FIXME drop.this
### 0.4.0.dev2 externalize recommended rules for updating app setting rules (240316 T12:00)

* `0.4.0.dev2` externalize recommended rules for updating app setting rules
    * [x] 1. created `xl2roefact/data/README_app_config_rules.md` containing the recommended rules for updating app setting rules
    * [x] 2. refer it in `config_settings.py` in its docstring section ==> exported `rules_content` that contain text
    * [x] 3. update `app_cli.py` module to load them accordingly on `settings --rules` command + option
    * [x] 4. build this package and publish on PyPi
    * archived locally (RLSE) package wheel & dist
    * [x] 5. update `xl2roefact README` to reflect that change
    * [x] 6. build all deliverables
    * [x] 7. update `downloads.md` with section for "Other resource downloads" with doc from item 1
* `240314piu01` update GitHub `ad hoc` workflow, made usable for any project component by moving structures to project root and letting environment management at command script glance
* `0.4.0.dev1` fixed `xl2roefact` CLI app version addressing
* `0.4.0.dev0` updated `xl2roefact.__init__.py` to expose public symbols
* `240313piu02` small administrative adjustments: update technical axl2roefact DLD, build site & republish (used version `0.4.0rc0` for whole system)
* `240313piu01` application tech optimizations: `rdinv.__all__` spec, `__init__.__version__` import and made available as xl2roefact global











# Archived CHANGELOGs

<details markdown="1"><summary markdown="1">
## 0.4 version
</summary>

* [0.4.0.dev2 externalize recommended rules for updating app setting rules (240316 T12:00)](
./changelog_history/CHANGELOG-0.4.0.dev2.m
)

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


