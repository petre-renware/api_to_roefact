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

# version objects
from . import __version__
from .__version__ import __doc__ as app_logo
from .__version__ import normalized_version as normalized_version

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

    # class variables for default session data values (used when no other data is provided and in all cases when a value is needed but is not known)
    file_name: str = "*.xlsx"
    invoice_type: InvoiceTypesEnum = InvoiceTypesEnum.NORMALA.value
    files_directory: Path =  "invoice_files/"
    owner_datafile: Path = None
    verbosity: bool = False

    
    def __init__(
        self, *,  # elipsis as default values help to make difference between a sent parameter (even with None) and a not sent one
        file_name: str = ...,
        invoice_type: InvoiceTypesEnum = ...,
        files_directory: Path = ...,
        owner_datafile: Path = ...,
        verbosity: bool = ...
        # TODO: need more patams from other commands ? 
    ):
        """Default session data variables.
        """
        #FIXME code here or drop me when clear plan specs
        '''#TODO plan
        - for None or not specified params init their instance value with class default values
        - otherwise call `self.session_data(...parametrs...)`
        '''
        ... #FIXME code here

    
    def session_data(
        self, *,  # elipsis as default values help to make difference between a sent parameter (even with None) and a not sent one
        file_name: str = ...,
        invoice_type: InvoiceTypesEnum = ...,
        files_directory: Path = ...,
        owner_datafile: Path = ...,
        verbosity: bool = ...
        # TODO: need more patams from other commands ? 
    ) -> bool:
        """Keep grouped session data as class instance variables.
        
        Persist instance variables for relevant parameters:
        * if a parameter is not sent at call, then it is left unchanged
        * if a parameter is sent with `None` value, then it is loaded with corresponding default value (from class variable)        

        Args;
            `data_item`: these are all data items required to be kept as reusable session data

        Return:
            `bool`: specify if operation was terminated normally
        """
        ...  #FIXME code here
        return True  # normal end with job done


    @classmethod
    def version(cls) -> str:
        """return the version of xl2roefact that is used by this class
        """
        return normalized_version()


    def xl2json(
        self,
        tbd  #TODO: rest of params
    ) -> ...:
        """read excel invoice and generate a JSON file with invoice data, miscellaneous meta and original Excel found data

        Args;
            `...`: ...

        Return:
            `...`: ...
        """
        ...  # TODO: code.me


    def settings(
        self,
        tbd  #TODO: rest of params
    ) -> ...:
        """read excel invoice and generate a JSON file with invoice data, miscellaneous meta and original Excel found data

        Args;
            `...`: ...

        Return:
            `...`: ...
        """
        ...  # TODO: code.me
