#!./.wenv_xl2roefact/bin/python3 #FIXME attn to this path if intend to move in modules/
""" xl2roefact - module to create a unified class for all xl2roefact and to be used as library by any other external systems

Identification:
    code-name: `xl2roefact`
    copyright: (c) 2023 RENWare Software Systems
    author: Petre Iordanescu (petre.iordanescu@gmail.com)

Deployments:
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
from rich import print
from rich.pretty import pprint

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
    print("[cyan]xl2roefact[/] application - convert invoice files from Excel format to JSON and XML")
    print("Support: [yellow]www.renware.eu, petre.iordanescu@gmail.com[/]")
    print("Copyright (c) 2023 RENware Software Systems.")
    print("[yellow]Usage:[/]")
    print("\tExtract Excel data into a JSON file with default configs: xl2roefact xl2json")
    print("\tObtain more help: xl2roefact --help")


@app_cli.command()
def settings():
    """display application configuration parameters and settings - subject to be changed by user"""
    with open("config_settings.py") as f:
        print(f.read())


@app_cli.command()
def xl2json(
    file_name: Annotated[
        str,
        typer.Option(
            default="*.xlsx",
            help="files to process (wildcards allowed)"
        )
    ] = "*.xlsx",
    excel_files_directory: Annotated[
        Path,
        typer.Option(
            "--files-directory", "-d",
            exists=True,
            file_okay=False,
            dir_okay=True,
            writable=True,
            readable=True,
            resolve_path=True,
            help="directory to be used to look for Excel files"
        ),
    ] = "invoice_files/",
    verbose: Annotated[
        bool,
        typer.Option(
            "--verbose", "-v",
            help="show detailed processing messages"
        ),
    ] = False
):  #TODO all args are subject of CONFIG and DOCUMENTATION
    """extract data from an Excel file (save data to JSON format file with the same name as original file but `.json` extension)
    """
    print(f"*** Component [red]xl2roefact[/] launched at {datetime.now()}")

    # process files as requested in command line
    tmp_files_to_process = Path(excel_files_directory)
    print(f"[yellow]INFO note:[/] files to process: [yellow]{Path(tmp_files_to_process, file_name)}[/]")
    list_of_files_to_process = list(tmp_files_to_process.glob(file_name))
    if verbose:
        print(f"[yellow]DEBUG note:[/] list object with files to process: [green]{list_of_files_to_process}[/]")
    for a_file in list_of_files_to_process:
        if verbose:
            print(f"[yellow]DEBUG note:[/] to process now: [green]{a_file}[/]")
        invoice_to_process = Path("./", a_file)  # current file name to process, starting from current directory (the `excel_files_directory` is already contained in)
        ret_val = rdinv(file_to_process=invoice_to_process, debug_info=verbose)
        if not ret_val:
            print(f"[yellow]INFO note:[/] last step returned an error and process could be incomplete. Please review previous messages.")


if __name__ == "__main__":
    app_cli()
