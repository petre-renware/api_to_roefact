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
from .__version__ import normalized_version as normalized_version

# general librarie
import dataclasses
from dataclasses import dataclass
from pathlib import Path
#FIXME.ck&drop from rich import print

# xl2roefact specific libraries
from .sys_settings import InvoiceTypesEnum


@dataclass
class SessionDataType:
    """define session data used in class `Commands`
    """
    file_name: str = None
    invoice_type: InvoiceTypesEnum = None
    files_directory: Path = None
    owner_datafile: Path = None
    verbosity: bool = None


class Commands:
    """xl2roefact commands interface.

    Methods:
        `session_data`: persist session data parameters sent to any command at its call in instance variables
        `version`: return the version of `xl2roefact` used by this class
        `settings`: implement command with the same name
        `xl2json`: implement command with the same name
        `command_n`: other commands short description
    """

    # default session data values (used when no other data is provided)
    # default values are only for "clear known" variables
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

    
    def session_data(
        self, *,  # elipsis as default values help to make difference between a sent parameter (even with None) and a not sent one
        file_name: str = ...,
        invoice_type: InvoiceTypesEnum = ...,
        files_directory: Path = ...,
        owner_datafile: Path = ...,
        verbosity: bool = ...,
        #TODO: more params from other commands
        **args
    ) -> bool:
        """Keep grouped session data as class instance variables.
        
        Persist instance variables for relevant parameters:
        * if a parameter is not sent at call, then it is left unchanged
        * if a parameter is sent with `None` value, then it is loaded with corresponding default value (from class variable)
        * *note* ref `**args`: other parametrs / data "not in specs" parameters but which need to be used by more commands in same session

        Args:
            `data_item`: these are all data items required to be kept as reusable session data

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


