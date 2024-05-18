"""Layer 2 **commands** implementation.

Objectives:

* create an environment wheree a xl2roefact can be run in *session or interactivelly mode*
* session parameters: persist commands run parameters in user profile (directory of `os.%userprofile%` or Linux `~/.profile`)
* group all layer 2 commands for:
    * `xl2roefactd` (aka server)
    * `xl2roefact-client` (aka console client)
    * `web2roefact` (aka web client UI front end)* components

Identification:

* code-name: `commands`
* Copyright: (c) 2024 RENware Software Systema
* Author: Petre Iordanescu (petre.iordanescu@gmail.com)
"""

#TODO get all imports from app_clu. see what keep here...
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
#FIXME.ck&drop from rich import print
from rich.pretty import pprint
from rich.markdown import Markdown
from rich.console import Console
# xl2roefact specific libraries
from .libutils import hier_get_data_file
from . import config_settings as configs  # configuration elements to use with `settings` command
from .rdinv import rdinv  # status #TODO: wip...
from .wrxml import wrxml  # status #FIXME: not yet started
from .chkxml import chkxml  # status #FIXME: not yet started
from .ldxml import ldxml  # status #FIXME: not yet started
from .chkisld import chkisld  # status #FIXME: not yet started
from .sys_settings import InvoiceTypesEnum


class Commands:
    """xl2roefact commands interface.
    """

    # default sessions data values (used when no other data is provided and in all cases when a value is needed but is not known)
    file_name: str = "*.xlsx"
    invoice_type: InvoiceTypesEnum = InvoiceTypesEnum.NORMALA.value
    files_directory: Path =  "invoice_files/"
    owner_datafile: Path = None

    
    def __init__(
    ):
        """Default session data variables.
        """
        
    def session_data(
        *,  # accept only named parameters
        file_name: str = None,
        invoice_type: InvoiceTypesEnum = None,
        files_directory: Path = None,
        owner_datafile: Path = None
        #TODO: need more patams from other commands ? 
    ) -> bool:
        """Keep grouped session data as class instance variables.
        Persist instance variables for relevant parameters (ie, not `None`)
        """
        
        '''data params of xl2json from app_cli. keep all
            
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
            file_okay=True,
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
        '''
        return True  # normal end with job done



