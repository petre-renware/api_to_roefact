"""*Layer 2 commands* implementation.

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
    verbose: bool = None


class Commands:
    """xl2roefact commands layer implementation. [Details here](../doc/README_xl2roefact_library.md)
    """

    # Default session data values (used when no other data is provided). Default values are only for "clear known" variables
    default_data = SessionDataType(
        file_name = "*.xlsx",
        invoice_type = InvoiceTypesEnum.NORMALA,
        files_directory =  "invoice_files/",
        owner_datafile = None,
        verbose = False
    )


    def __init__(self):
        """Init session data variables with default values.
        """
        self.session_data = SessionDataType()
        self.session_data_reset()  # get default values


    def session_data_set(
        self, *,
        file_name: str = ...,
        invoice_type: InvoiceTypesEnum = ...,
        files_directory: Path = ...,
        owner_datafile: Path = ...,
        verbose: bool = ...
    ) -> bool:
        """Set session data.

        Rules:
        * session data is kept as class-instance variables. This will use for "interactive" or "web" editions
        * if a parameter is not sent at call, then it is left unchanged
        * any other sent value is saved as instance variable
        * elipsis as default parametrs values help to make difference between a sent parameter (even with None) and a not sent one

        Args:
            `all_item`: more instances = all data items required to be kept as reusable session data

        Return:
            `bool`: any change was made
        """
        ret_code = False
        if file_name != ...:
            self.session_data.file_name = file_name
            ret_code = True
        if invoice_type != ...:
            self.session_data.invoice_type = invoice_type
            ret_code = True
        if files_directory != ...:
            self.session_data.files_directory = files_directory
            ret_code = True
        if owner_datafile != ...:
            self.session_data.owner_datafile = owner_datafile
            ret_code = True
        if verbose != ...:
            self.session_data.verbose = verbose
            ret_code = True
        return ret_code


    def session_data_reset(self):
        """Resset session data to defaults.
        """
        self.session_data = dataclasses.replace(__class__.default_data)


    @classmethod
    def version(cls) -> str:
        """return the version of `xl2roefact` used by this class
        """
        return xl2roefact_version


    def xl2json(
        self,
        invoice_type: InvoiceTypesEnum  = ...,
        file_name: str = ...,
        files_directory: Path = ...,
        owner_datafile: Path = ...,
        verbose: bool = ...
    ) -> bool:  #FIXME what returns? at least: console messages & execution state (ie, did or not something)
        """read excel invoice and generate a JSON file with invoice data, miscellaneous meta and original Excel found data

        Args:
            `invoice_type_code`: invoice type (for example regular invoice or storno) as this info is not usually subject of Excel file. Default to `380` (regular / usual invoice)
            `file_name`: files to process (wildcards allowed).
            `files_directory`: directory to be used to look for Excel files. Defaults to `invoice_files/`. NOTE: if default directory does not exists will consider current directory instead
            `owner_datafile`: File to read invoice supplier (owner) data instead Excel.
            `verbose`: show detailed processing messages". Defaults to `False`.

        Return:
            `...`: ...
        """
        # for not specified parameters get default values from session_data:
        #     - if a_parameter == ...:  get params from session data
        #     - esle: save param to session data (helps to avoid parameters repeating in same session) 
        if invoice_type == ...:
            invoice_type = self.session_data.invoice_type
        else:
            self.session_data.invoice_type = invoice_type
        if file_name == ...:
            file_name = self.session_data.file_name
        else:
            self.session_data.file_name = file_name
        if files_directory == ...:
            files_directory = self.session_data.files_directory
        else:
            self.session_data.files_directory = files_directory
        if owner_datafile == ...:
            owner_datafile = self.session_data.owner_datafile
        else:
            self.session_data.owner_datafile = owner_datafile
        if verbose == ...:
            verbose = self.session_data.verbose
        else:
            self.session_data.verbose = verbose
        #
        # core function process
        console = Console() #TODO: redirect out to a file a variable to collect and return it at finish...
        console.print(f"*** Application [red]xl2roefact[/] launched at {datetime.now()}")
        # prep Excel files to rocess as requested in command line (NOTE: if default directory does not exists will consider current directory instead)
        tmp_files_to_process = Path(files_directory)
        if not (tmp_files_to_process.exists() and tmp_files_to_process.is_dir()):
            tmp_files_to_process = Path(".").absolute()
            console.print(f"[dark_orange]WARNING note:[/] Default directory not found. Will consider current directory: [cyan]{tmp_files_to_process}[/].")
        if verbose:
            console.print(f"[yellow]INFO note:[/] files to process: [cyan]{Path(tmp_files_to_process, file_name)}[/]")
            console.print()
        list_of_files_to_process = list(tmp_files_to_process.glob(file_name))  # `glob()` will unify in a list with specified files as pattern
        # process Excel files list
        for a_file in list_of_files_to_process:
            rdinv_run_messages = list()  # this will collect rdinv running messages and if verbose is True will print
            invoice_to_process = Path("./", a_file)  # current file name to process, starting from current directory (the `files_directory` is already contained in)
            # prep for owner data acquiring from external data-file or from Excel
            full_path_owner_datafile = None
            if owner_datafile is not None:  # prep are to call `rdinv()` module with parameter to read supplier data from external file instead Excel
                full_path_owner_datafile = hier_get_data_file(owner_datafile)
                if full_path_owner_datafile:
                    ... #FIXME code in dropping => remain else
                    '''
                    invoice_datadict = rdinv(
                        invoice_type_code=invoice_type,
                        file_to_process=invoice_to_process,
                        debug_info=rdinv_run_messages,
                        owner_datafile=full_path_owner_datafile
                    )
                    if verbose:
                        for msg in rdinv_run_messages:
                            console.print(msg)
                    '''
                else:
                    console.print(f"[red]ERROR: Owner data file ([cyan]{owner_datafile}[/]) is not valid or does not exists. Process terminated.[/].")
                    return  # just exit...
            else:
                ... #FIXME code in dropping => branch useless
                '''
                invoice_datadict = rdinv(
                    invoice_type_code=invoice_type,
                    file_to_process=invoice_to_process,
                    debug_info=rdinv_run_messages
                )
                if verbose:
                    for msg in rdinv_run_messages:
                        console.print(msg)
                '''
            ... #FIXME mvd code
            invoice_datadict = rdinv(
                invoice_type_code=invoice_type,
                file_to_process=invoice_to_process,
                debug_info=rdinv_run_messages,
                owner_datafile=full_path_owner_datafile
            )
            if verbose:
                for msg in rdinv_run_messages:
                    console.print(msg)
            ... #FIXME mvd code
            if not invoice_datadict:
                console.print(f"[yellow]INFO note:[/] last step returned an empty invoice JSON and process could be incomplete. Please review previous messages.")
        # end of core function process
        return ... #TODO see what you defined for return ...


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


