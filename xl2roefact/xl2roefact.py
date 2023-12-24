#!./.venv/bin/python3 #FIXME attn to this path if intend to move in modules/
"""xl2roefact - module to create a unified class for all xl2roefact and to be used as library by any other external systems.

Identification:
    code-name: `xl2roefact`
    copyright: (c) 2023 RENWare Software Systems
    author: Petre Iordanescu (petre.iordanescu@gmail.com)

Deployments:
    Windows: `xl2roefact.msi` MSI installer package with EXE x386 CLI application
    Linux: `xl2roefact` executable wrapper shell for `xl2roefact.py` application

Specifications:
    command general format: `xl2roefact [file(s)-to-convert] COMMAND [OPTIONS]`
    help: `xl2roefact [COMMAND] --help`
"""


from xl2roefact import app_cli


if __name__ == "__main__":
    app_cli.run()



