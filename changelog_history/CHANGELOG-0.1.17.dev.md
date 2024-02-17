**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.1.17.dev


### 0.1.17.dev fixed all application & package running standard ways (231224 h05:30)

* 231224piu_a made cli app to run as: Python package main app (`python -m xl2roefact`) and as script (`python xl2roefact.py`) while still letting the Python library `xl2roefact` as importable and use in a programmatic way:
    * [x] make `.../xl2roefact/app_cli.py` (from actual `.../xl2roefact/__main__.py`) which is complete code of CLI app plus a `run()` function that just launch it
    * [x] make `.../xl2roefact/__main__.py` that just import `app_cli` for `run()` function and call it
    * [x] change actual `<xl2roefact ROOT/>xl2roefact.py` to import `xl2roefact.app_cli` for `run()` function and call it
    * [x] test for MSI package builds ref `<xl2roefact ROOT/>xl2roefact.py`
    * [x] clean code, test and close issue:
        * `python xl2roefact.py [OPTIONS] COMMAND [ARGS]...`
        * `python -m xl2roefact [OPTIONS] COMMAND [ARGS]...`

* 231223piu_a multiple changes ref main code: `xl2roefact.py` and library `xl2roefact`, MAINLY created `xl2roefact/__main__.py` as normal of xl2roefact.py










