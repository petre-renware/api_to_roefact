"""**xl2roefact.__main__**: Python package standard file to assure run as `python -m xl2roefact`.

Identification:

* code-name: `__main__`
* copyright: (c) 2023 RENWare Software Systems
* author: Petre Iordanescu (petre.iordanescu@gmail.com)

Deployments:

* Windows:  MSI installer with EXE application.
* Linux: `xl2roefact` executable shell as wrapper for `xl2roefact.py`.

Specifications:

* command general format: `python -m xl2roefact [OPTIONS] COMMAND [ARGS]... `.
* help: `python -m xl2roefact --help`.
"""


from xl2roefact import app_cli


if __name__ == "__main__":
    app_cli.main()



