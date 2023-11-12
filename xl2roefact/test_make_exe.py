""" xls2xml - Module wrapper to assure full generation of XML file for ANAF RO E-Fact (file `f-XML`)

Identification:
    code-name: xls2xml
    copyright: (c) 2023 RENWare Software Systems
    author: Petre Iordanescu (petre.iordanescu@gmail.com)

Deploymens:
    Windows: `xls2xml.exe` portable x386 CLI application
    Linux: `xls2xml` executable CLI shell

Specifications:
    command general format: `xls2xml [COMMND] [OPTIONS] file(s)-to-convert`
    built in help: `xls2xml [COMMAND] --help`
"""





import typer


''' #TODO plan
- create `app` version to be able to create multiple commnads with same CLI executable
- ...
'''


def main(name: str):
    print(f"Hello {name}") #FIXME test - drop me when start final version


if __name__ == "__main__":
    typer.run(main)

