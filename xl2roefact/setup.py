""" setup for `xl2roefact` package configuration in order to build Windows MSI & EXE and PyPy package.

Identification:
* code-name: `setup.py`
* copyright: (c) 2023 RENWare Software Systems
* author: Petre Iordanescu (petre.iordanescu@gmail.com)

Specifications:
* INITIAL create `build/` directory with all building commands for _xl2roefact_ app: `python setup.py build`
* @RELEASE create MSI package in `dist/`: `python setup.py bdist_msi`
* *helper*: see official doc here `https://cx-freeze.readthedocs.io/en/latest/setup_script.html`
"""

import sys
from cx_Freeze import setup, Executable
#TODO **iss001**: part of code here as commentes
#import xl2roefact.__version__.py as ver
#PACKAGE_VERSION = ver.__version__


# Dependencies are automatically detected, but it might need fine tuning
build_options = {"packages": [], "excludes": []}

base = "console"

executables = [
    Executable("xl2roefact.py", base=base)
]

setup(
    options = {
        "build_exe": build_options,
        #TODO **iss001** here to get the version from `xl2roefact/__version__.py`:
        #"version": PACKAGE_VERSION,
    },
    executables = executables
)
