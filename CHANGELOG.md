<small>**RENware Software Systems**</small>

**INVOICEtoROeFact** Project

[TOC]


# CHANGELOG

- For version code structure meaning see SDEVEN methodology document
- with _(F)_ are marked those changes that are features in order to be copied in a RELNOTE file and with _(B)_ bug fixes from versions released
- publishing is made under `publishing` branch
- `<PROJECT ROOT>/doc_src/` is the default starting location in a file path (if not clear from context) (**ATTN** - in production environment is `docs/`)
- `<WEB_ROOT>/` is the HTTP server root directory, as default `docs/` and supposed if no other parent is specified


<!--#FIXME uncomment when finish 0.3...
## 0.4 (TODO:.next)

```
    - ---[ #TODO general planning board ]---:
    * -#NOTE link Swagger servicii web: `https://mfinante.gov.ro/web/efactura/informatii-tehnice`
    * -#NOTE link specif API incarcare fact: `https://mfinante.gov.ro/static/10/eFactura/upload.html#/EFacturaUpload/handleRequest`
    -
    * ---[ FUTURE NEW APP COMMANDS ]---:
        * `config` - set `config_settings.py` variables (make it INTERACTIVELY using `Rich prompt`)
        * `xl2json` - crt_wip... (last upd @ 240219piu_a)
        * `json2xml` - see module WRXML,
        * `json2pdf` - new module. tbd..,
        * `xml2roefact` - see module LDXML
        * chk for other commands from doc `https://invoicetoroefact.renware.eu/commercial_agreement/110-SRE-api_to_roefact_requirements.html#componenta-xl2roefact`
    -
    * -#NOTE Plan for `rdinv` module:
        * [ ] invoice supplier (`<cac:AccountingSupplierParty>`)
    -------------------------------------------------------------------------------------------------
```

### TODO:next... 0.4.0rc invoice supplier (#NOTE: date here...)

* tbd.Must... @RELEASE update version files & [follow `/RELEASE-QA_checklist.md`](./RELEASE-QA_checklist.md)

* tbd.Must... `xl2roefact` need to make invoice supplier (`<cac:AccountingSupplierParty>`) - MANDATORY to plan for next version
* tbd.Could... define `xl2roefact` entry points and/or scripts. comments in `xl2roefact/setup.py` ref exec scripts with installed package
* tbd.Should... [piu @_240126] left in `xl2roefact/setup.py` comments & example ref how to ___pre-set MSI build meta information___ / parameters (obj: default target dir where install, path registration, icon, ...)
-->









## 0.3 (NOTE:...wip...)

### NOTE:...wip... 0.3.2b single EXE version (#NOTE: date here...)

* tbd.Must... @RELEASE update version files & [follow `/RELEASE-QA_checklist.md`](./RELEASE-QA_checklist.md)
* tbd Should... update `app_cli`, option `--version` to get normalized version string

* wip... `240308piu01` make single EXE with `pyinstaller`
    * [x] 1. ck & install `pyinstaller` in local environment. Update it if neccesary
    * [x] 2. adhoc try to execute it. Make a command for (`build_sexe`)
          RESULTS: `.../xl2roefact/dist/xl2roefact/.. ` with exe & various files
    * [x] 3. created a PDM script for command `build_sexe`
    * [x] 4. result produced in `...dist/xl2roefact/dist/` - a little bit unacceptable but ok for that step
    * [x] 5. adjust command `build_sexe` to produce a single file EXE
          RESOLUTION: up here resulted one file `xl2roefact.exe` in `.../dist/` directory
    * [x] 6. adjust command `build_sexe` to produce exe in other-tenp directory for name processing (req here in nxt item-step)
    * [x] 7. installed `packaging` package and updated `xl2roefact.__version__` module with function `normalized_version(raw_version: str) -> str`
    * [x] 8. adjust command `build_sexe` to produce right file name as `xl2roefact-0.3.1.b1-win64.exe` and move it in `.../dist/` dir. Specs:
        - [x] in pyproject.toml make `post_build_sexe` entry of call type `{call = "xl2roefact.libutils:complete_sexe_file()"}`
        - [x] update `__version__` modules to accommodate this function
        - [x] skeleton rdy `libutils` module for function `complete_sexe_file()` that rename and move resulted exe file: .../dist_sexe/xl2roefact_to_update_name.exe` --> `.../dist/xl2roefact-version-win64.exe`
        - [x] finalize & test code of `complete_sexe_file()` ==> PASS
    * [ ] 9. in `pyproject.toml` include `build_sexe` cmd in `build_all`
    * [ ] x. build single exe for current stable version of xl2roefact = `0.3.1b1`
    * [ ] x. update `downloads.md` to include single exe resource starting with last stable version = `0.3.1b1`
    * [ ] x. update site
* `240307piu01` xl2roefact pdm environment created a script for **build PyPi** operation. PDM run script CAN be used from local development environment but CANNOT be used in build_pypi automation, at execution raise error that cannot execute mkdir on branch - NOT ANALYZED, just reverted workflow to previous one
* `230406piu08` updated `downloads.md` ref end-of-life date of all `0.1...` versions: 10-March-2024






<!--#NOTE: to be archived ASAP -->

### 0.3.1b1 fixed bug JSON->["Invoice"]["cac_InvoiceLine"] list[list] (230306 h19:30)

* `230406piu07` release version:
     * [x] 1. update xl2roefact version
     * [x] 2. build new app
     * [x] 3. update downloads.md doc
     * [x] 3. build site
     * [x] 4. publish on PyPi
* `230406piu06` FIXED `240306piu05` ref JSON->["Invoice"]["cac_InvoiceLine"] list[list] bug by transforming in 1-dimensional list using strategy from `TO FIX -> item 3`. TEST PASS.
* `240306piu05` TEST POINT: converted online the invoice JSON file to XML ==> `Fact_Petrom_11017969.xml`. **RESOLUTIONS:**
    * ATTN: the usable part is strict those related to "Invoice" key, any other information is not relevant and will not be included in application generated XML
    * TO FIX: JSON generated key "cac_InvoiceLine" is list[list] the first list being obsolete (just item 0 which is the effective list). Proposals:
        * 1. at XML generation to preserve only `cac_InvoiceLine[0]` - *pro*: SIMPLE, REASONABLE, LATERAL EFFECTS FREE - *cons*: JSON file remain for this key as "non-intuitive" information
        * 2. re-engineer `rdinv.py` to generate right info structure for this key - *pro*: right and intuitive JSON information presentation - *cons*: a lot of lateral effects, there is "a lot of code" that already extract only item 0 and this code could be in functions out of `rdinv.py` module, for example in `libutils.py`
        * 3. update module `rdinv.py` to preserve only index 0 **when create key `cac_InvoiceLine`, line ~408 so:**
            - ACTUAL value: `"cac_InvoiceLine": copy.deepcopy(tmp_InvoiceLine_list),`
            - DESIRED value:
                ```python
                "cac_InvoiceLine": copy.deepcopy(tmp_InvoiceLine_list)[0],
                ```
* `240306piu04` archived 0.3.0b & 0.3.1b versions














# Archived CHANGELOGs

<details markdown="1"><summary markdown="1">
## 0.3 version
</summary>

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


