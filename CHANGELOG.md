<small>**RENware Software Systems**</small>

**INVOICEtoROeFact** Project

[TOC]


# CHANGELOG

- For version code structure meaning see SDEVEN methodology document
- with _(F)_ are marked those changes that are features in order to be copied in a RELNOTE file and with _(B)_ bug fixes from versions released
- publishing is made under `publishing` branch
- `<PROJECT ROOT>/doc_src/` is the default starting location in a file path (if not clear from context) (**ATTN** - in production environment is `docs/`)
- `<WEB_ROOT>/` is the HTTP server root directory, as default `docs/` and supposed if no other parent is specified


### General PLAN

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




### TODO:...wip 0.4.0??? invoice supplier (#NOTE: ...date_here...)

* tbd.Must... @RELEASE update version files & [follow `/RELEASE-QA_checklist.md`](./RELEASE-QA_checklist.md)

* tbd.Must... `xl2roefact` need to make invoice supplier (`<cac:AccountingSupplierParty>`) - MANDATORY to plan for next version
* tbd.Could... define `xl2roefact` entry points and/or scripts. comments in `xl2roefact/setup.py` ref exec scripts with installed package
* tbd.Should... [piu @_240126] left in `xl2roefact/setup.py` comments & example ref how to ___pre-set MSI build meta information___ / parameters (obj: default target dir where install, path registration, icon, ...)

* wip... (last used `240311piu02`)
















<!--#NOTE: to be archived -->

## 0.3

### 0.3.2b0 single EXE version (240311 h16:30)

???+ info "Release versions"
    * xl2roefact: "0.3.1b1"
    * web2roefact: "n/a"
    * invoice_template: "0.1.20"
    * INVOICEtoROefact: "0.3.2b0"

* `240311piu02` run script build_doc to update ref `libutils.py` module. Update & publish site.
* `240311piu01` update `downloads.md` to include single exe resource starting with last stable version = `0.3.1b1`
* `240308piu00` update `app_cli`, option `--version` to get normalized version string
* `240308piu01` make single EXE with `pyinstaller`
    * [x] 1. ck & install `pyinstaller` in local environment. Update it if necessary
    * [x] 2. adhoc try to execute it. Make a command for (`build_sexe`)
          RESULTS: `.../xl2roefact/dist/xl2roefact/.. ` with exe & various files
    * [x] 3. created a PDM script for command `build_sexe`
    * [x] 4. result produced in `...dist/xl2roefact/dist/` - a little bit unacceptable but ok for that step
    * [x] 5. adjust command `build_sexe` to produce a single file EXE
          RESOLUTION: up here resulted one file `xl2roefact.exe` in `.../dist/` directory
    * [x] 6. adjust command `build_sexe` to produce exe in other-temp directory for name processing (req here in nxt item-step)
    * [x] 7. installed `packaging` package and updated `xl2roefact.__version__` module with function `normalized_version(raw_version: str) -> str`
    * [x] 8. adjust command `build_sexe` to produce right file name as `xl2roefact-0.3.1.b1-win64.exe` and move it in `.../dist/` dir. Specs:
        - [x] in pyproject.toml make `post_build_sexe` entry of call type `{call = "xl2roefact.libutils:complete_sexe_file()"}`
        - [x] update `__version__` modules to accommodate this function
        - [x] skeleton rdy `libutils` module for function `complete_sexe_file()` that rename and move resulted exe file: .../dist_sexe/xl2roefact_to_update_name.exe` --> `.../dist/xl2roefact-version-win64.exe`
        - [x] finalize & test code of `complete_sexe_file()` ==> PASS
    * [x] 9. in `pyproject.toml` include `build_sexe` cmd in `build_all`
    * [x] 10. build single exe for current stable version of xl2roefact = `0.3.1b1`. Updated tech doc DLD (xl2roefact API Reference)
    * [x] 11. FIX: single exe not work. FIX: Must to HAVE DIFFERENT NAME THAN DIRECTORY `xl2roefact/`. Created copy `xl2roefact_copy_for_sexe.py` for xl2roefact.py to be used by pyinstaller in build_sexe script. **This file should be kept on as a perfect copy of original** (as sym-link doesn't work).
* `240307piu01` xl2roefact pdm environment created a script for **build PyPi** operation. PDM run script CAN be used from local development environment but CANNOT be used in build_pypi automation, at execution raise error that cannot execute mkdir on branch - NOT ANALYZED, just reverted workflow to previous one
* `230406piu08` updated `downloads.md` ref end-of-life date of all `0.1...` versions: 10-March-2024










# Archived CHANGELOGs

<details markdown="1"><summary markdown="1">
## 0.3 version
</summary>

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


