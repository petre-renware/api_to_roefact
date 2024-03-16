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

#FIXME.drop.me.after.`0.4.0.dev2` from xl2roefact import __version__ as ver
from xl2roefact.__version__ import normalized_version
import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need fine tuning
build_options = {"packages": [], "excludes": []}

base = "console"

executables = [
    Executable("xl2roefact.py", base=base)
]


#TODO: pct.1*) Example of how pre-set MSI build options.
# NOTE: to be compared with command line arguments / options can be sent
# NOTE: obj are:
#    -1) to install by default in "C:\ProgramFiles...\xl2roefact\"
#    -2) to have the PATH set so can use app from any directory
#    -3) optional to have icon, copyright , license ...
'''
bdist_msi_options_definition = {
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


#TODO: pct.2*) varianta de punct de exec din/cu pachet instalat bazat pe script Python parte din pachet sau dependentele acestuia
# vezi si `https://stackoverflow.com/questions/4840182/setup-py-and-adding-file-to-bin`
'''
entry_points_definition = {
    'console_scripts': [
        'command-name = package.module:main_func_name',                  
    ],              
},
'''


# TODO: pct.3*) varianta de pubcte de intrare "de orice tip de executabil de oriunde ar fi pe acea masina"
# vezi si `https://stackoverflow.com/questions/4840182/setup-py-and-adding-file-to-bin`
'''
scripts_definition = ['scripts/xmlproc_parse', 'scripts/xmlproc_val']
'''





setup(
    options = {"build_exe": build_options},
    #FIXME.drop.me.after.`0.4.0.dev2` version = ver.__version__,
    version = normalized_version(),
    executables = executables,
    # bdist_msi_options = bdist_msi_options_definition,  # NOTE: pct.1*) ref `bdist_msi_options`  
    # entry_points = entry_points_definition,  # NOTE: pct.2*)
    # scripts = scripts_definition  # NOTE pct.3*)
)




