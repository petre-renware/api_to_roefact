#!../.venv/bin/python3
"""app_cli: the command line application for all xl2roefact functionalities.

Identification:
* code-name: `xl2roefact`
* copyright: (c) 2023 RENWare Software Systems
* author: Petre Iordanescu (petre.iordanescu@gmail.com)

Deployments:
* Windows:  MSI installer with EXE application.
* Linux: `xl2roefact` executable shell as wrapper for `xl2roefact.py`.

Specifications:
* command general format: `xl2roefact [file(s)-to-convert] COMMAND [OPTIONS]`.
* help: `xl2roefact [COMMAND] --help`.
"""


# general libraries
import typer
import os
import sys
from typing_extensions import Annotated
from pathlib import Path
from typing import Optional
from datetime import datetime
from rich import print
from rich.pretty import pprint

# xl2roefact specific libraries
from xl2roefact import __version__ as appver
import xl2roefact.config_settings as configs  # configuration elements to use with `settings` command
from xl2roefact.rdinv import rdinv  # status #TODO: wip...
from xl2roefact.wrxml import wrxml  # status #FIXME: not yet started
from xl2roefact.chkxml import chkxml  # status #FIXME: not yet started
from xl2roefact.ldxml import ldxml  # status #FIXME: not yet started
from xl2roefact.chkisld import chkisld  # status #FIXME: not yet started



""" CLI builder section.
"""
app_cli = typer.Typer(name="xl2roefact")


@app_cli.command()
def about():
    """provide a short application description.
    """
    version_string = appver.__version__
    app_logo = appver.__doc__
    # logo & version
    print(app_logo)
    print(f"xl2roefact {version_string} application by RENware Software Systems (c) 2023, 2024")
    # about details
    print("[yellow]extract & convert Excel invoice files to JSON, XML and upload info to [cyan]RO ANAF e-Fact[/] system")
    print("Support: [yellow]www.renware.eu, petre.iordanescu@gmail.com[/]")
    print("Product code: [yellow]0000-0095[/]")
    #print("Copyright (c) 2023, 2024 RENware Software Systems.")
    print("Usage: for detailed help use [yellow]xl2roefact --help[/]")


@app_cli.command()
def settings():
    """display application configuration parameters and settings that are subject to be changed by user.
    """
    print("\nApplication current settings are:\n---------------------------------------")
    list_of_settings = dir(configs)
    for i in list_of_settings:
        if i == i.upper():  # preserve only items supposed to be defined like CONSTANTS
            val_of_i_item = eval("configs." + i)
            print(f"[yellow]{i}[/] = {val_of_i_item}")


@app_cli.command()
def xl2json(
    file_name: Annotated[
        str,
        typer.Argument(
            help="files to process (wildcards allowed)"
        )
    ] = "*.xlsx",
    files_directory: Annotated[
        Path,
        typer.Option(
            "--files-directory", "-d",
            exists=False,
            file_okay=False,
            dir_okay=True,
            writable=True,
            readable=True,
            resolve_path=True,
            help="directory to be used to look for Excel files (if default directory does not exists will consider current directory instead)."
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
    """extract data from an Excel file (save data to JSON format file with the same name as original file but `.json` extension).

    Args:
        `file_name`: files to process (wildcards allowed).
        `files_directory`: directory to be used to look for Excel files. Defaults to `invoice_files/`. NOTE: if default directory does not exists will consider current directory instead
        `verbose`: show detailed processing messages" Defaults to `False`.
    """
    print(f"*** Application [red]xl2roefact[/] launched at {datetime.now()}")

    # process files as requested in command line (NOTE: if default directory does not exists will consider current directory instead)
    tmp_files_to_process = Path(files_directory)
    if not (tmp_files_to_process.exists() and tmp_files_to_process.is_dir()):
        tmp_files_to_process = Path(".").absolute()
        print(f"[dark_orange]WARNING note:[/] Default directory not found. Will consider current directory instead: [cyan]{tmp_files_to_process}[/].")
    print(f"[yellow]INFO note:[/] files to process: [cyan]{Path(tmp_files_to_process, file_name)}[/]")
    list_of_files_to_process = list(tmp_files_to_process.glob(file_name))  # `glob()` will unify in a list with specified files as pattern
    if verbose:
        print(f"[yellow]DEBUG note:[/] list object with files to process: [green]{list_of_files_to_process}[/]")
    for a_file in list_of_files_to_process:
        if verbose:
            print(f"[yellow]DEBUG note:[/] to process now: [green]{a_file}[/]")
        #
        invoice_to_process = Path("./", a_file)  # current file name to process, starting from current directory (the `files_directory` is already contained in)
        invoice_datadict = rdinv(file_to_process=invoice_to_process, debug_info=verbose)
        if not invoice_datadict:
            print(f"[yellow]INFO note:[/] last step returned an error and process could be incomplete. Please review previous messages.")
        #
        if verbose:
            print(f"[yellow]DEBUG note:[/] `xl2roefact` module, content of resulted `invoice` data dictionary:")
            pprint(invoice_datadict)
            print()



@app_cli.callback(invoke_without_command=True)
def called_when_no_command(
    ctx: typer.Context,
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            help="show application version"
        ),
    ] = False
):
    """function called when no command is invoked and to provide only application version (for external users to test it!).
    """
    if (ctx.invoked_subcommand is None) and not version:
        print("[red]No command. Please use --help to get help.[/]")
        sys.exit(0)
    version_string = appver.__version__
    if version:
            print(f"xl2roefact {version_string}")




def main():
    app_cli()

if __name__ == "__main__":
    main()

