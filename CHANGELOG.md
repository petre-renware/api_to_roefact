<small>**RENware Software Systems**</small>

**INVOICEtoROeFact** Project

[TOC]


# CHANGELOG

- For version code structure meaning see SDEVEN methodology document
- with _(F)_ are marked those changes that are features in order to be copied in a RELNOTE file and with _(B)_ bug fixes from versions released
- publishing is made under `publishing` branch
- `<PROJECT ROOT>/doc_src/` is the default starting location in a file path (if not clear from context) (**ATTN** - in production environment is `docs/`)
- `<WEB_ROOT>/` is the HTTP server root directory, as default `docs/` and supposed if no other parent is specified



## 0.3 (TODO: wip...)

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
    -------------------------------------------------------------------------------------------------
```




### wip... 0.3.2b single EXE version (#NOTE: date here...)

* tbd.Must... @RELEASE update version files & [follow `/RELEASE-QA_checklist.md`](./RELEASE-QA_checklist.md)

* tbd.Must... `xl2roefact` need to make invoice supplier (`<cac:AccountingSupplierParty>`) - MANDATORY to plan for next version

* tbd.Could... define `xl2roefact` entry points and/or scripts. comments in `xl2roefact/setup.py` ref exec scripts with installed package
* tbd.Should... [piu @_240126] left in `xl2roefact/setup.py` comments & example ref how to ___pre-set MSI build meta information___ / parameters (obj: default target dir where install, path registration, icon, ...)

* tbd.Must... make single EXE with `pyinstaller`


* tbd.NOW... can refer in gh `0.3.0b` release notes the file `changelog_history/CHANGELOG-0.3.0b.md`

* wip.... (las used 240306piu03)













### 0.3.1b promote `0.3.0b0` deliverables: WHEEL, TRA.GZ, MSI to `0.3.1b`

* `240306piu03` build all components, `downloads.md`, build site and republish on PyPi. Archived locally
* `240306piu02` promote `0.3.0b0` deliverables: WHEEL, TRA.GZ, MSI to `0.3.1b`
* `240306piu01` archived locally all `0.3.0b` deliverables: WHEEL, TRA.GZ, MSI, repository tag




<!--#NOTE: piu@240306 said: 0.3.0b kept for commodity reasons and should be dropped max after 15.mar.2024 or when next release available -->
### 0.3.0b xl2roefact invoice taxes summary (240306 07:00)

* `240302piu03` invoice taxes summary:
    * ref doc `xl2roefact/invoice_files/_PLAN_model...xml`, lines 91-104)
    * prepared place in rdinv() search "NOTE: ....place intended for `cac:TaxTotal`" line ~413
    * [x] 1. prepared a work file `xl2roefact/tests/__wk_invoice_tax_total.md` with dev specs & TODOs
    * [x] 2. defined calculation formulas in `xl2roefact/tests/__wk_invoice_tax_total.md`
    * [x] 3. made a function skeleton `invoice_taxes_summary(invoice_lines: list[dict])` in `libutils` that calculates whole required structure. Receive as parameter the `Invoice dict` part related to items list, ie existing variable `tmp_InvoiceLine_list`
    * [x] 4. calculated `cac_TaxTotal` calculation code of item 3. in function `libutils.invoice_taxes_summary(...)`. Code test PASS. Function closed
    * [x] 5. updated XML-JSON map
    * [x] 6. calculated cbc_TaxAmount
    * [x] 7. update JSON example used in documentation
    * [x] 8. updated version number of xl2roefact app (component & mkdocs.yml)
    * [x] 9. run `pdm build_all` ==> version deliverables incl DLD doc
    * [x] 10.a update `downloads.md` with `0.3.0b` deliverables
    * [x] 10.b build site & publish
    * [x] 10.c publish library on PyPi (use CI workflow by branch `pypi-publish`)
    * [x] 11. clean code, drop `xl2roefact/tests/__wk_invoice_tax_total.md
* `240301piu02` refactored `xl2roefact/invoice_files/` to `xl2roefact/refact_xml_models_and_specs/`
* `240302piu01` updated `xl2rofact.rdinv` function, area commented "...build final structure..." created variable `_tmp_reusable_items: dict` to keep "partial variables" that are calculated and potentially will be reused in next code
* `240301piu_01` set all workflows `run-name`














# Archived CHANGELOGs

<details markdown="1"><summary markdown="1">
## 0.3 version
</summary>

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


