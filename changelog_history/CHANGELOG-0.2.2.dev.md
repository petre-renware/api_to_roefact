**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.2.2.dev


### 0.2.2.dev project development environment improvements (240229 h19:00)

* `240229piu01` updated `.../downloads.md` for xl2roefact section to link PyPi for versions `>= 0.2.1b` and let WHEEL & DIST as "Download package source"
* `240228piu04` improved `xl2roefact python library` API Reference document ref to TOC and Title
* `240228piu03` project review, cleanup and update: workflows, useless files, TODO & FIXME comments, etc...
* `240228piu02` FIXED main project for use with PDM. `pdm update` command successfully run. **RESOLUTION: pdm can be used in main project as package manager. Should run locally to create venv and must update it with pdm update.** 10xG!
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



