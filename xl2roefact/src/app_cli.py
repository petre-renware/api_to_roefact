#! /usr/bin/env python3
"""app_cli: the command line application for all xl2roefact functionalities.

Identification:

* copyright: (c) 2023 RENWare Software Systems
* author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

# version objects
from .__version__ import __doc__ as app_logo
from .__version__ import normalized_version

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
from rich.markdown import Markdown
# xl2roefact specific libraries
from .libutils import hier_get_data_file
from . import config_settings as configs  # configuration elements to use with `settings` command
from .rdinv import rdinv  # status #TODO: wip...
from .wrxml import wrxml  # status #FIXME: not yet started
from .chkxml import chkxml  # status #FIXME: not yet started
from .ldxml import ldxml  # status #FIXME: not yet started
from .chkisld import chkisld  # status #FIXME: not yet started
from .sys_settings import InvoiceTypesEnum


""" CLI builder section.
"""
app_cli = typer.Typer(name="xl2roefact")




@app_cli.command()
def about():
    """Provide a short application description.
    """
    version_string = normalized_version()
    print(Markdown(app_logo))
    print(f"xl2roefact {version_string} application by RENware Software Systems (c) 2023, 2024")
    # about details
    print("[yellow]extract & convert Excel invoice files to JSON, XML and upload info to [cyan]RO ANAF e-Fact[/] system")
    print("Support: [yellow]www.renware.eu, petre.iordanescu@gmail.com[/]")
    print("Product code: [yellow]0000-0095[/]")
    print("Usage: for detailed help use [yellow]xl2roefact --help[/]")




@app_cli.command()
def settings(
    rules: Annotated[
        bool,
        typer.Option(
            "--rules", "-r",
            help="show settings recommended update rules"
        ),
    ] = False
):
    """Display application configuration parameters and settings that are subject to be changed by user.

    Args:
    
        `rules`: show recommended rules to follow when change application configurable settings (available in both RO & EN languages). Defaults to `False`.
    """

    if rules:  # show configuration rules from module docstring
        from .config_settings import rules_content
        print(rules_content)  # content is already rendered
        print()  # print a blank line for readability
    print("\nCurrent settings:\n-------------------------------")
    list_of_settings = dir(configs)
    for i in list_of_settings:
        if i == i.upper():  # preserve only items supposed to be defined like CONSTANTS
            val_of_i_item = eval("configs." + i)
            print(f"[yellow]{i}[/] = {val_of_i_item}")




@app_cli.command()
def xl2json(
    invoice_type: InvoiceTypesEnum  = InvoiceTypesEnum.NORMALA.value,
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
    owner_datafile: Annotated[
        Path,
        typer.Option(
            "--owner-datafile", "-o",
            exists=False,
            file_okay=False,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=False,
            help="File to read invoice supplier (owner) data instead Excel."
        ),
    ] = None,
    verbose: Annotated[
        bool,
        typer.Option(
            "--verbose", "-v",
            help="show detailed processing messages"
        ),
    ] = False
):
    """Extract data from an Excel file (save data to JSON format file with the same name as original file but `.json` extension).

    Args:

        `invoice_type_code`: invoice type (for exaple regular invoice or storno) as this info is not usually subject of Excel file. Default to `380` (regular / usual invoice)
        `file_name`: files to process (wildcards allowed).
        `files_directory`: directory to be used to look for Excel files. Defaults to `invoice_files/`. NOTE: if default directory does not exists will consider current directory instead
        `owner_datafile`: File to read invoice supplier (owner) data instead Excel.
        `verbose`: show detailed processing messages". Defaults to `False`.
    """
    print(f"*** Application [red]xl2roefact[/] launched at {datetime.now()}")
    # process files as requested in command line (NOTE: if default directory does not exists will consider current directory instead)
    tmp_files_to_process = Path(files_directory)
    if not (tmp_files_to_process.exists() and tmp_files_to_process.is_dir()):
        tmp_files_to_process = Path(".").absolute()
        print(f"[dark_orange]WARNING note:[/] Default directory not found. Will consider current directory: [cyan]{tmp_files_to_process}[/].")
    print(f"[yellow]INFO note:[/] files to process: [cyan]{Path(tmp_files_to_process, file_name)}[/]")
    list_of_files_to_process = list(tmp_files_to_process.glob(file_name))  # `glob()` will unify in a list with specified files as pattern
    if verbose:
        print(f"[yellow]DEBUG note:[/] list object with files to process: [green]{list_of_files_to_process}[/]")
    for a_file in list_of_files_to_process:
        if verbose:
            print(f"[yellow]DEBUG note:[/] to process now: [green]{a_file}[/]")
        #
        invoice_to_process = Path("./", a_file)  # current file name to process, starting from current directory (the `files_directory` is already contained in)
        if owner_datafile is not None:  # prep are to call `rdinv()` module with parameter to read supplier data from external file instead Excel
            full_path_owner_datafile = hier_get_data_file(owner_datafile)
            if full_path_owner_datafile:
                invoice_datadict = rdinv(
                    invoice_type_code=invoice_type,
                    file_to_process=invoice_to_process,
                    debug_info=verbose,
                    owner_datafile=full_path_owner_datafile
                )
            else:
                print(f"[red]ERROR: Owner data file ([cyan]{owner_datafile}[/]) is not valid or does not exists. Process terminated.[/].")
                return  # just exit...
        else:
            invoice_datadict = rdinv(
                invoice_type_code=invoice_type,
                file_to_process=invoice_to_process,
                debug_info=verbose
            )
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
            "--version", "-V",
            help="show application version"
        ),
    ] = False
):
    """Application global information (command agnostic).
    """
    if (ctx.invoked_subcommand is None) and not version:
        print("[red]No command. Please use --help to get help.[/]")
        sys.exit(0)
    version_string = normalized_version()
    if version:
        print(f"xl2roefact {version_string}")




def main():
    app_cli()

run = app_cli  # NOTE: for `run` "reason to be" as copy of `app_cli` see iss `0.1.22b 240216piu_a`


if __name__ == "__main__":
    main()

