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
from xl2roefact import __version__ as ver
import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need fine tuning
build_options = {"packages": [], "excludes": []}

base = "console"

executables = [
    Executable("xl2roefact.py", base=base)
]


#TODO: Example of how pre-set MSI build options.
# NOTE: to be compared with command line arguments / options can be sent
# NOTE: obj are:
#    -1) to install by default in "C:\ProgramFiles...\xl2roefact\"
#    -2) to have the PATH set so can use app from any directory
#    -3) optional to have icon, copyright , license ...
'''
bdist_msi_options = {
    "data": {
        "ProgId": [
            ("Prog.Id", None, None, "This is a description", "IconId", None),
        ],
        "Icon": [
            ("IconId", "icon.ico"),
        ],
    },
}
'''


#TODO: varianta de punct de exec pachet instalat bazat pe script Python parte din pachet sau dependentele acestuia
'''
entry_points = {
    'console_scripts': [
        'command-name = package.module:main_func_name',                  
    ],              
},
'''




setup(
    options = {"build_exe": build_options},
    version = ver.__version__,
    executables = executables,
    entry_points = {
        'console_scripts': [
            'command-name = package.module:main_func_name',                  
        ],              
    },
)




