**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.1.19.dev


### 0.1.19.dev invoice customer and partial invoice total values calculations (240116 h06:00)

* 2401_xl2roefact_doc_01 `xl2roefact` update technical documentation, file `xl2roefact/doc/810.05a-xl2roefact_component.md`

* 240112piu_b 95% clean code `rdinv()` from customer area identification, from line 204 (kept a DBG print just for area identification (useful for next task ref the same opers but for Supplier))

* 240112piu_a module `app_cli.py`, created `called_when_no_command(...)` function called when no command is invoked and to provide only application version (for external users to test it!)

* 240110piu_c `xl2json` `about` command to get version & "nice" LOGO from `xl2roefact/__version__.py`, vars `__version__` & `__doc__`

* 240110piu_b `xl2roefact/setup.py`ref get app version from file when build EXE/MSI test for `__version__` is correctly get and release

* 240110piu.a reviewed & updated `xl2roefact` package `README.md` + `xl2roefact/__version__.py` with an app logo and for text mistyping bugs

* 240108piu_c changed `pyproject.toml` for auto update package version from file `xl2roefact/__version__.py` (see also opiss 240108piu_b)

* 240108piu_b created `xl2roefact/__version__` file that contains variable `__version__` with INTENTION to use in `pyproject.toml` for app version key (in a future issue)

* 240108piu_a more items:
    * `config_settings.py` created entry `PATTERN_FOR_PARTNER_ADDRESS` & updated `rdinv` module in constants area
    * add comments in `app_cli.py` ref `def_inv_dir` issue &&...
    * updated environment dependencies and installed `pyinstaller` development package with intention to make "single EXE" application to be able to run "from USB stick"

* 240107piu_a reviewed `xl2roefact` package `README.md`:
    - (c) explained proposed & promoted directory structure used by CLI application
    - (b) short invoice JSON file structure
    - (a) created first version of tutorial section

* 240106piu_a invoice customer search and persist for "RegistrationName"



