**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.3.2b0


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


