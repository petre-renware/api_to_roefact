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
from .__version__ import __version__ as xl2roefact_version
#FIXME.drop.id.unused... from .__version__ import normalized_version as normalized_version

# general librarie
import dataclasses
from dataclasses import dataclass
from pathlib import Path
#FIXME.drop.id.unused... from rich import print
from typing import Optional
from datetime import datetime
from rich import print
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
# xl2roefact specific libraries
from .sys_settings import InvoiceTypesEnum




@dataclass
class SessionDataType:
    """Define session data used in class `Commands`
    """
    file_name: str = None
    invoice_type: InvoiceTypesEnum = None
    files_directory: Path = None
    owner_datafile: Path = None
    verbosity: bool = None


class Commands:
    """xl2roefact commands layer implementation.

    More [details here](../doc/README_xl2roefact_library.md)
    """

    # Default session data values (used when no other data is provided). Default values are only for "clear known" variables
    default_data = SessionDataType(
        file_name = "*.xlsx",
        invoice_type = InvoiceTypesEnum.NORMALA.value,
        files_directory =  "invoice_files/",
        owner_datafile = None,
        verbosity = False
    )

    
    def __init__(self):
        """Init session data variables with default values.
        """
        self.session_data = dataclasses.replace(__class__.default_data)

    
    def session_data_set(
        self, *,
        file_name: str = ...,
        invoice_type: InvoiceTypesEnum = ...,
        files_directory: Path = ...,
        owner_datafile: Path = ...,
        verbosity: bool = ...
    ) -> bool:
        """Set session data.
        
        Rules:
        * session data is kept as class-instance variables. This will be useful for "interactive" or "web" editions
        * if a parameter is not sent at call, then it is left unchanged
        * any other sent value is saved as instance variable
        * elipsis as default parametrs values help to make difference between a sent parameter (even with None) and a not sent one
        
        Args:
            `all_item`: more instances = all data items required to be kept as reusable session data

        Return:
            `bool`: specify if operation was terminated normally
        """
        # test if parameter sent to update its value
        ... #FIXME code here
        # otherwise (not sent) ignore it (ket unchanged / untouched)
        ... #FIXME code here
        return True  # normal end with job done


    @classmethod
    def version(cls) -> str:  #FIXME test.me
        """return the version of `xl2roefact` used by this class
        """
        return xl2roefact_version


    def xl2json(
        self,
        tbd  #TODO: rest of params
    ) -> ...:
        """read excel invoice and generate a JSON file with invoice data, miscellaneous meta and original Excel found data

        Args:
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

        Args:
            `...`: ...

        Return:
            `...`: ...
        """
        ...  # TODO: code.me





    #
    # utility internal / not public class objects
    #
    @classmethod
    def get_var_name(cls, var):  #FIXME test.me
        """Return a variable defined in class as string of its name.
        """
        for name, value in locals().items():
            if value is var:
                return name


