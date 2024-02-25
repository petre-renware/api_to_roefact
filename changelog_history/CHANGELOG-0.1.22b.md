**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.1.22b


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



