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
        * `xl2json` - crt_wip... (last upd @ 240123)
        * `json2xml` - see module WRXML,
        * `json2pdf` - new tbd..,
        * `xml2roefact` - see mpdule LDXML
        * chk for other commands from doc `https://apitoroefact.renware.eu/commercial_agreement/110-SRE-api_to_roefact_requirements.html#componenta-xl2roefact`
    -
    * -#NOTE_PLAN `rdinv` module:
        * invoice header
            * [...] wip... @ `§240219piu_a` invoice header - customer bank, RegCom, email, tel, ...
            * [ ] invoice header - supplier (`<cac:AccountingSupplierParty>`)
            * [ ] invoice grand totals (there was left a comment ref whole XML structure in rdinv(), line # ~ where build & write "Invoice" key)
    -------------------------------------------------------------------------------------------------
```




### #TODO..._wip... 0.2.0 xl2roefact invoice customer info-optional items (bank, email, reg-com, phone) (#NOTE upd ".dev" qualifier & set date here...)

* tbd.Must... @RELEASE [follow `/RELEASE-QA_checklist.md`](./RELEASE-QA_checklist.md)

* wip.Would... automate GitHub site build & publishing. Last attempt @`240216piu_a`.

* tbd.Should... [piu_240126] left in `setup.py` comments & example ref how to ___pre-set MSI build meta information___ / parameters (obj: default target dir where install, path registration, ...)

* tbd.Must... publish `xl2roefact` package --> read PDM doc ref package release

* tbd.Could... init a PDM simple env in project root. Keep in mind:
    * root project is for SITE GENERATION. ? the `web2roefact` will need its own directory5like `xl2roefact` ?
    * as consequence the project name is **INVOICEtoROefact**
    * and the version is last from CHANGELOG

* wip...

* ...wip.Must... 240219piu_a invoice customer search for other keys: "reg com", "bank / IBAN / cont", "phone", "email"
    * [x] 1. read req informnation and stored in local vars, as full dict (for excel original key) and as cleaned (for invoice key)
    * [x] 2. store info in customer_header_area --> excel original data key
    * [ ] 3. store info in customer_header_area --> Invoice key
    * [ ] 4. test app and its results
    * [ ] 5. update DLD documentation & build xl2roefact
    * [ ] 6. update site documentation ...if needed / something new to say :) ...
    * [ ] 7. test, publish & test again

* 240218piu_b created an automation workflow to run `xl2roefact xl2json` in directory `xl2roefact/tests/` and to obtain JSON of invoice to test it
    * [x] 1. moved test Excel invoices from `.../xl2roefact/invoice_files/` to `.../xl2roefact/tests/`
    * [x] 2. created automation YAML file (`run_xl2roefact.yml`)
    * [x] 3. test ==> PASS (exec results + `stdout --> _test_results.txt` written on `xl2roefact/tests/`)
* 240218piu_a documentation improvements by using dropdown items






















## 0.1 (closed 240217 h21:30)

### 0.1.22b xl2roefact application interface improvements (240217 h12:00)

* 240217piu_b updated site with new `0.1.22b` deliverables, `xl2roefact CLI, WHEEL & DIST`
* 240217piu_a automated build of xl2roefact artifacts (on merge to branch `build-xl2roefact`)
* 240214piu_b make in site a dedicated page for downloads: "Help --> Downloads" and refer it in all places where downloads are intended
* 240216piu_a automated GitHub site build & publishing. FIXED ERROR: `mkdocs_typer._exceptions.MkDocsTyperException: 'run' must be a 'typer.main.Typer' object, got <class 'function'>` was changed `run` object to `app_cli` one
* 240214piu_c.BUGFIX ref `240213piu_a.FAILED` fixed & enabled `.github/.../ci.yml`. To test by merging to `build`
* 240214piu_a xl2roefact component (`.../app_cli.py`) function `settings(...)` add `--rules` option (param) to display `config_settings.__doc__`
* 240213piu_a.FAILED merged for `/requirements.txt` lief package update as OK-PAS & disabled gh-workflow by renaming `ci.yml` to `ci.yml temp_disabled`. Actions tried:  (-1.) updated `.gh-workflow.../ci.yml`  (-2.) "small change" in `/README.md` in copyright year to test  (-3.) merge to `build` branch for test
* 240212piu_e.BUGFIX navigation "xl2roefact --> Referinta CLI" (file `/mkdocs.yml`). Updated `xl2roefact/README.md` add a `<a id="comenzile-aplicatiei"></a>` after header "## Comenzile aplicatiei" paragraph "Detalii comenzi:" and ref it accordingly in mkdocs.yml navigation following HTML file, not MARKDOWN one
* 240212piu_d rebuild all deliverables `pdm build_all` ==> v0.1.22 MSI, WHL, SDIST & moved them to a dedicated `_WIP_0.1.22_/` until decide to rebuild or keep
* 240212piu_c added navigation "xl2roefact --> Referinta CLI" (file `/mkdocs.yml`). Built & published site (`mkdocs build`).
* 240212piu_b updated `.../xl2roefact/app_cli.py` to format app logo string as markdown. Updated packages (`pdm build_all`).
* 240212piu_a review and updated xl2roefact logo (file: `...xl2roefact/__version__`). Updated API Reference doc (`pdm build_doc`). Clean project of obsolete files & open issues






### 0.1.21.post3 cleaned system documentation and site (240211 h23:59)

* 240211piu_b tested & reviewed `240211piu_a` ==> published site
* 240211piu_a upated `xl2roefact/README.md` clean section "Instalarea", preserved only Windows and Linux specs to run CLI component, ie, dropped library references as irrelevant at this point
* 240210piu_b test for iss `240210piu_a` ==> PASS
    * [x] app as functional (there are updates in code),
    * [x] re-build tech doc (`pdm build_doc`),
    * [x] build & publish site
* 240210piu_a reviewed & updated all `xl2roefact` modules for their docstring
* 240209piu_c updated `xl2roefact` component, README file, restructured info ref JSON file format (dropped redundant info)
* 240209piu_b reviewed & corrected `240209piu_a, 240208piu_a`. Published site
* 240209piu_a updated `xl2roefact *` documentation to drop redundant info (badges, prev versions useless details)
* 240208piu_a updated `xl2roefact library` documentation, docstring(s) and `mkdocs.yml` navigation entries to clarify subjects by using specific technical terms (this component address technical users not business ones)
* 240207piu_b improve site readability by detailed description at bullet items level and dropping / moving in other parts the content non "end user related" from: `/README.md`, `doc_src/.../810.05a-system_components.md`
* 240207piu_a updated all site in pages references to system components & deliverables version






### 0.1.21.post2 xl2roefact app detailed section with commands & options "--help" like (240206 h23:59)

* 240206piu_c test & release: -- create release, -- publish site, -- save deliverable archives
* 240206piu_b install package: `pip install mkdocs-typer` & upd back `requirements.txt`
* 240206piu_a add `mkdocs-typer` extension and update `xl2roefact/README.md`, section `Comenzile aplicatiei` page with generated documentation by this plugin






### 0.1.21.post1 fixed missing links in site root index page (240203 h10:30)

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












# Archived CHANGELOGs


<details markdown="1"><summary markdown="1">
## 0.1 version
</summary>

<!--#TODO collect rest of 0.1 items here... List of them; -->
Items not yet reviewed, extracted and archived:

* `0.1.22b` xl2roefact application interface improvements
* `0.1.21.post3` cleaned system documentation and site
* `0.1.21.post2` xl2roefact app detailed section with commands & options "--help" like
* `0.1.21.post1` fixed missing links in site root index page
* `0.1.21` rollout news in system portal invoicetoroefact.renware.eu

Items reviewed and archived:

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


