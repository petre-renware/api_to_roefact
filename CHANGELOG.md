<small>**RENware Software Systems**</small>

**INVOICEtoROefact** Project

[TOC]


# CHANGELOG

- For version code structure meaning see SDEVEN methodology document
- with _(F)_ are marked those changes that are features in order to be copied in a RELNOTE file and with _(B)_ bug fixes from versions released
- publishing is made under `publishing` branch
- `<PROJECT ROOT>/doc_src/` is the default starting location in a file path (if not clear from context) (**ATTN** - in production environment is `docs/`)
- `<WEB_ROOT>/` is the HTTP server root directory, as default `docs/` and supposed if no other parent is specified



## 0.2 (-#NOTE_wip...)

```
    - ---[ #TODO general planning board ]---------------------------
    * ai un exemplu complet si complet agnostic (trimis Gigi) de factura format XML si PDF tiparit ca sa faci: (1) incarcare XML (2) geenrare PDF (3) compararea variantelor si identificarea schemei XSD + document specificatii ANAF ref sistemul E-Factura (PDF trimis Liviu)
    * -#NOTE link Swagger servicii web: `https://mfinante.gov.ro/web/efactura/informatii-tehnice`
    * -#NOTE link specif API incarcare fact: `https://mfinante.gov.ro/static/10/eFactura/upload.html#/EFacturaUpload/handleRequest`

    - ---[ #TODO short planning board ]---------------------------
    * left OPEN ISSUES on: `0.1.7` release (and drop them when fixed).
      ...Aici descrierea pe scurt: in file `xl2roefact\invoice_files/_PLAN_model_test_factura_generat_anaf.xml`, line 114:_ `<cbc:ID>S</cbc:ID> #FIXME clarify.me_ pare a fi TIPUL PRODUSULUI: (S)erviciu sau ??? (P)rodus sau ???`
    -
    * ... FUTURE NEW APP COMMANDS :
        * `config` - set `config_settings.py` variables (make it INTERACTIVELY using `Rich prompt`)
        * `xl2json` - crt_wip... (last upd @ 240219piu_a)
        * `json2xml` - see module WRXML,
        * `json2pdf` - new module. tbd..,
        * `xml2roefact` - see module LDXML
        * chk for other commands from doc `https://invoicetoroefact.renware.eu/commercial_agreement/110-SRE-api_to_roefact_requirements.html#componenta-xl2roefact`
    -
    * -#NOTE Plan for `rdinv` module:
        * [ ] invoice supplier (`<cac:AccountingSupplierParty>`)
        * [... wip.`0.2.2b`] invoice taxes summary
    -------------------------------------------------------------------------------------------------
```




### #TODO_wip... 0.2.2b xl2roefact invoice taxes summary (#NOTE: date here...)

* tbd.Must... @RELEASE update version files & [follow `/RELEASE-QA_checklist.md`](./RELEASE-QA_checklist.md)

* tbd.Should... [piu @_240126] left in `xl2roefact/setup.py` comments & example ref how to ___pre-set MSI build meta information___ / parameters (obj: default target dir where install, path registration, icon, ...)
* tbd.Could... idem comments in `xl2roefact/setup.py` ref exec scripts with installed package

* tbd.Could... check how use SECRETs in gh actions (ref PyPi publish workflow token used)

* tbd.Must... there is one more summary ref taxes (doc `xl2roefact/invoice_files/_PLAN_model...xml`, lines 91-104):
```xml
<cac:TaxTotal>  #TODO tbd...
    <cbc:TaxAmount currencyID="RON">190.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
        <cbc:TaxableAmount currencyID="RON">1000.00</cbc:TaxableAmount>
        <cbc:TaxAmount currencyID="RON">190.00</cbc:TaxAmount>
        <cac:TaxCategory>
            <cbc:ID>S</cbc:ID>
            <cbc:Percent>19.00</cbc:Percent>
            <cac:TaxScheme>
                <cbc:ID>VAT</cbc:ID>
            </cac:TaxScheme>
        </cac:TaxCategory>
    </cac:TaxSubtotal>
</cac:TaxTotal>
```

* tbd.Must... update `.../downloads.md` for xl2roefact Python area to point to PyPi for versions starting with `0.2.1b` and make this link agnostic to WHEEL or DIST as PyPi will decide best option

* wip...

* `240228piu01` created a mechanism to run adhoc commands *for xl2roefact component*:
    * [x] skeleton windows-cmd-file to be run by adhoc script (usable as template) `xl2roefact/tests/adhoc.cmd` (NOTE: running OS = Windows)
    * [x] workflow `adhoc-run.yml` to install pdm environment & run `./tests/adhoc.cmd &>./tests/_test_results.txt` (with crt directory `xl2roefact/`) triggered by merge to branch `adhoc`. Run results (stdout) written to `./tests/_test_results.txt`
    * [x] documented this feature in `/README_git_automation_tools.md`
* `240227piu01` improve xl2roefact package documenting the PyPi link to package (`https://pypi.org/project/xl2roefact/`)
* `240226piu04` published `xl2roefact` package & created automation workflow. Steps;
    * [x] 0. updated workflow `pypi-publish.yml` to run on brach `pypi-publish`
    * [x] 1. change workflow code to move `.msi` files in a temporary directory, execute publish then get back moved files
    * [x] 2. drop directories for versions `0.1.18/` & `0.1.19/`
    * [x] 3. test packages publish. FAILED.
    * [x] 4. update `doc_src/.../downloads.md` ref crt item 2.
    * [x] 5. build & publish site
    * [x] 6. update `pyproject.toml` to update classifiers list according to approved standard
    * [x] 7. update workflow to ignore all old / previous packages (not compliant "classifiers" section)
    * [x] 8. TEST PASS, here running messages: 
      ```
      Uploading xl2roefact-0.2.1b0-py3-none-any.whl = 100% 
      Uploading xl2roefact-0.2.1b0.tar.gz = 100%
      ```
    * [x] 9. clean workflow code, update `pyproject.toml` with site URL
* `240226piu03` updated root `pyproject.toml` (project `INVOICEtoROefact`) ref `xl2roefact` dependency and ref development dependencies section
* `250226piu02` created empty /draft workflow `pypi-publish.yml` to be used to PyPi publish `xl2roefact` python packages.
    * Project publisher was registered on PyPi @ `https://pypi.org/manage/account/publishing/` for GitHub repository `INVOICEtoROefact`.
    * Declared PyPi project name: `xl2roefact`
    * PyPi status: `Pending publishers` @ 240226 06:00
* `250226piu01` improved documentation "visibility" with INVOICEtoROefact components features






### 0.2.1b xl2roefact invoice values summary (240225 h18:30)

* `240221piu_a` invoice grand totals
    * [x] 1. new function `dict_sum_by_key(...)` to sum a dict at all levels for a key. Implemented in `xl2roefact libutils` module.
    * [x] 2. doc with wk.specs ref summary structure `.../xl2roefact/tests/_tmp_wkdoc_invoice_summary.md` (NOTE: will be deleted after finish)
    * [x] 3. created work JSON-XML map required structure in `.../xl2roefact/tests/__invoice_summary.md`
    * [x] 4. code for some calculations, test & fix formulas
    * [x] 5. update JSON-XML map in code (rdinv.py)
* `200220piu_b` init a PDM simple env in project root
    * [x] 1. root project is for SITE GENERATION
    * [x]  2. project name set to **INVOICEtoROefact** and the version dynamic from `/__version__.py`
    * [x] 3. updated `pyproject.toml` default dependencies
    * [x] 4. incomplete finalized PDM usage. Run `pdm init` then `pdm update` to get dependencies
      _RESOLUTION:_ item 4. will be finalied in next releases because is a long run task under Windows
* `240220piu_a` reorganized `INVOICEtoROeFact` project by preparing python directory structure for **`web2roefact`** component as installable package (model xl2roefact)









# Archived CHANGELOGs


<details markdown="1"><summary markdown="1">
## 0.2 version
</summary>

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


