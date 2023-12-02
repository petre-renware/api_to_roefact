#!./.wenv_xl2roefact/bin/python3 #FIXME attn to this path if intend to move in modules/
""" xl2roefact - module to create a unified class for all xl2roefact and to be used as liibrary by any other external systems

Identification:
    code-name: `xl2roefact`
    copyright: (c) 2023 RENWare Software Systems
    author: Petre Iordanescu (petre.iordanescu@gmail.com)

Deploymens:
    Windows: `xl2roefact.exe` portable x386 CLI application
    Linux: `xl2roefact` executable CLI shell

Specifications:
    command general format: `xl2roefact [file(s)-to-convert] COMMAND [OPTIONS]`
    help: `xl2roefact [COMMAND] --help`
"""


# general libraries
import typer
import os
from typing_extensions import Annotated
from pathlib import Path
from typing import Optional
from datetime import datetime
from colorama import Fore, Back, Style
from pprint import pprint

# xl2roefact specific libraries
from rdinv import rdinv  # status #TODO: wip
from wrxml import wrxml  # status #FIXME: not yet started
from chkxml import chkxml  # status #FIXME: not yet started
from ldxml import ldxml  # status #FIXME: not yet started
from chkisld import chkisld  # status #FIXME: not yet started


""" CLI builder section
"""
app_cli = typer.Typer(name="xl2roefact")


@app_cli.command()
def about():
    """short application description"""
    typer.echo(f"{Fore.CYAN}xl2roefact{Style.RESET_ALL} application - convert invoice files from Excel format to JSON and XML")
    typer.echo(f"Support: {Fore.YELLOW}www.renware.eu, petre.iordanescu@gmail.com{Style.RESET_ALL}")
    typer.echo(f"Copyright (c) 2023 RENware Software Systems.")
    typer.echo(f"{Fore.YELLOW}Usage:{Style.RESET_ALL}")
    typer.echo(f"\tJust xl2json with default configs: xl2roefact xl2json")
    typer.echo(f"\tObtain more help: xl2roefact --help")


@app_cli.command()
def settings():
    """display application configuration parameters and settings - subject to be changed by user"""
    with open("config_settings.py") as f:
        print(f.read())


# FIXME #NOTE @231130
""" the function should have these options:
    - [ ] ...wip... `file_name`; argument, pathlib.Path, optional, default "*", validators: is file, exists, ...
    - [ ] new. `--config_file`; option, pathlib.Path, default "config_set..." (check), validators: is file, exists, readable, ...
"""  # NOTE #FIXME


@app_cli.command()
def xl2json(
    file_name: Annotated[str, typer.Argument()] = "*.xlsx",
    excel_files_directory: Annotated[
        Path,
        typer.Option(
            exists=True,
            file_okay=False,
            dir_okay=True,
            writable=True,
            readable=True,
            resolve_path=True,
            help="directory to be used to look for Excel files",
        ),
    ] = "invoice_files/",
):  # TODO all args are subject of CONFIG and DOCUMENTATION
    """extract data from an Excel file (save data to JSON format file with the same name as original file but `.json` extension)"""
    typer.echo(f"*** Component {Fore.RED}xl2roefact{Style.RESET_ALL} launched on {Fore.GREEN}{datetime.now()}{Style.RESET_ALL}")
    typer.echo(f"{Fore.YELLOW}INFO note:{Style.RESET_ALL} directory where to search Excel files is set to: {Fore.GREEN}{excel_files_directory}{Style.RESET_ALL}")

    print(f"{Fore.YELLOW}INFO note:{Style.RESET_ALL} ARGUMENT {Fore.GREEN}{file_name=}{Style.RESET_ALL}")  #NOTE for debug purposes
    #raise typer.Abort()  #FIXME - drop me after tests
    #TODO use `excel_files_directory` + / + `file_name` to find all files and process them in a loop
    #TODO use `glob.glob(....)` as here `https://docs.python.org/2/library/glob.html`
    #NOTE processing is like for RENware invoice && Kraftanlagen invoice (next code lines, #100..#105):

    #NOTE for test --- RENware invoice #FIXME solve it when set ARGUMENT `file_name`
    invoice_to_process = os.path.join(excel_files_directory, "fact_RENF1004.xlsx")
    rdinv(file_to_process=invoice_to_process)
    #NOTE another test --- Kraftanlagen invoice #FIXME solve it when set ARGUMENT `file_name`
    invoice_to_process = os.path.join(excel_files_directory, "Fact _Petrom_11017969.xlsx")
    rdinv(file_to_process=invoice_to_process)


if __name__ == "__main__":
    app_cli()
