**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.1.9.dev

### 0.1.9 `xl2roefact.RDINV` running executable and distribution kit (231203 h07:00)

* 231103piu_b releasing ==> made `dist/0.1.9-exe.win-amd64-3.10.zip` with executable file

* 231103piu_a `xl2roefact.py` more updates:
    * [x] set verbose flag for debugging mode
    * [x] made `file_name` argument as file(s) to be processed with wildcards like Python standard function `os.glob.glob()` (reference here `https://docs.python.org/2/library/glob.html`)
    * [x] build a new fresh executable in `build/exe.win-amd64-3.10/`

* 231202piu_b `xl2roefact.py` started a skeleton for `file_name` argument - see code-in-file @"TODO here to use `excel_files_directory` + / + `file_name` to find all files and process them in a loop"

* 231202piu_a build complete `cxFreeze` configuration in order to build Windows executable and installer package (as `msi` package):
    * [x] create a minimal setup (`setup.py`)
    * [x] create `build/` directory with all building commands for _xl2roefact_ app: `python setup.py build` (see official doc here `https://cx-freeze.readthedocs.io/en/latest/setup_script.html`)
    * **CONCLUSION** `msi` package OK, `exe` file NOK - see `setup.py` for a detailed comment marked `NOTE-[piu@231202]`



