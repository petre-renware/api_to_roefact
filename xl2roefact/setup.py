#!./.wenv_xl2roefact/bin/python3
""" a minimal setup for `cxFreeze` configuration in order to build Windows executable and installer package (as `msi` package)

    Identification:
        code-name: `setup.py`
        copyright: (c) 2023 RENWare Software Systems
        author: Petre Iordanescu (petre.iordanescu@gmail.com)

    Specifications:
        - create `build/` directory with all building commands for _xl2roefact_ app: `python setup.py build`
        - *helper*: see official doc here `https://cx-freeze.readthedocs.io/en/latest/setup_script.html`
"""

import sys
from cx_Freeze import setup, Executable


'''#FIXME NOTE-[piu@231202]
    1.- `build/` directory contains an executanble that not run !!!
    2.- it generates the msi package (`dist/xl2roefact-0.1.0-win64.msi`)
    3.- msi package runs OK and install executable, but is the executable produced at (1.-) and dpes not run (in fact run but does absolutelly nothing)
'''



# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'console'

executables = [
    Executable('xl2roefact.py', base=base)
]

setup(name='xl2roefact',
      version = '0.1',
      description = 'Excel invoice upload to RO E-Fact system',
      options = {'build_exe': build_options},
      executables = executables)
