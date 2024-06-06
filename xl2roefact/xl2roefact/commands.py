"""*Layer 2 commands* API implementation.

Objectives:

* create an environment where a xl2roefact can be run in *session or interactivelly mode*
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
import copy
import dataclasses
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Any
from datetime import datetime, timezone, tzinfo, timedelta
from rich import print
from rich.pretty import pprint
from rich.markdown import Markdown
from rich.console import Console
from collections import deque

# xl2roefact specific libraries
from .libutils import hier_get_data_file
from . import config_settings as configs  # configuration elements to use with `settings` command
from .rdinv import rdinv
from .sys_settings import InvoiceTypesEnum




@dataclass
class CommandResult:
    """Define the result of execution. This structure contains information collected in methods execution.
    After each method execution all "prints" and status information stated by method in its execution (ie, which was saved) will be contained in.

    Fields:
    * `status_code`: `int` Status code as used by HTTP standard returned codes (200 for success)
    * `status_timestamp`: `str` Timestamp of information in UTC ISO format
    * `status_text`: `str` Short text of this result set. Normally used to display a brief message note associated to code (for example "404 Not found")
    * `result`: `Any` The effective result information returned by method as core result of execution. Depending on method, this is a *Python specific structure*, scalar, basic or complex one
    * `stdout_text`: `str` Collected console "prints" output in text format. Normally a standard print() of this value will reproduce the exact console output if method would be "raw executed" in development mode
    * `stdout_html`: `str` the same as `stdout_text` but in HTML format ready to be sent "as is" to a browser (its a COMPLETE and FULL HTML doc). Used if pages together with other elements it is recommended to isolate it with distinct `div` and `iframe` tags
    """
    status_code: int = None
    status_timestamp: str = None
    status_text: str = None
    result: Any = None
    stdout_text: str = None
    stdout_html: str = None

@dataclass
class SessionDataType:
    """Define session data used in class `Commands`.
    These data objects mainly represents almost all parameters 
    encountered in console application and that are suspect to 
    be reusable when "chain more commands" iin the same session 
    and is desirable to keep last values.
    
    Also in web applications is normal to not ask for parameters 
    already entered by an end user and to preserve last entered values 
    at least as default ones.
    """
    file_name: str = None
    invoice_type: InvoiceTypesEnum = None
    files_directory: Path = None
    owner_datafile: Path = None
    verbose: bool = None


class Commands:
    """xl2roefact commands layer implementation. [Descriere generala layer si componenta.](../doc/README_xl2roefact_library.md).
    """

    # Default session data values (used when no other data is provided). Default values are only for "clear known" variables
    default_data = SessionDataType(
        file_name = "*.xlsx",
        invoice_type = InvoiceTypesEnum.NORMALA,
        files_directory =  "invoice_files/",
        owner_datafile = None,
        verbose = False
    )
    # default rich.Console variable designed to collect all session stdout prints
    console: Console = Console(record=True)


    def __init__(self):
        """Init session data variables with default values.
        """
        #FIXME.drop.this.after.tst self.console = __class__.console  # initialize a new console
        self.session_data = SessionDataType()
        self.session_data_reset()  # get default values
        self.session_results = deque()
        self.response = CommandResult()  # prepare an ampty result to be used by/in command execution
        self.response_out(
            status_code = 200,
            status_text = "xl2json command started",
            status_result = None
        )


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
        if file_name is not ...:
            self.session_data.file_name = file_name
            ret_code = True
        if invoice_type is not ...:
            self.session_data.invoice_type = invoice_type
            ret_code = True
        if files_directory is not ...:
            self.session_data.files_directory = files_directory
            ret_code = True
        if owner_datafile is not ...:
            self.session_data.owner_datafile = owner_datafile
            ret_code = True
        if verbose is not ...:
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
    ) -> bool:
        """read excel invoice and generate a JSON file with invoice data, miscellaneous meta and original Excel found data

        Args:
            `invoice_type_code`: invoice type (for example regular invoice or storno) as this info is not usually subject of Excel file. Default to `380` (regular / usual invoice)
            `file_name`: files to process (wildcards allowed).
            `files_directory`: directory to be used to look for Excel files. Defaults to `invoice_files/`. NOTE: if default directory does not exists will consider current directory instead
            `owner_datafile`: File to read invoice supplier (owner) data instead Excel.
            `verbose`: show detailed processing messages". Defaults to `False`.

        Return:
            `bool`: True if command executed without errors. If return in False, the kasr result should be inspected to see error status and text (method `results_stack_pop()`)
        """
        # for not specified parameters get default values from session_data:
        #     - IF any parameter is `...`: get params from session data
        #     - ELSE: save param to session data (helps to avoid parameters repeating in same session)
        if invoice_type is ...:
            invoice_type = self.session_data.invoice_type
        else:
            self.session_data_set(invoice_type = invoice_type)
        if file_name is ...:
            file_name = self.session_data.file_name
        else:
            self.session_data_set(file_name = file_name)
        if files_directory is ...:
            files_directory = self.session_data.files_directory
        else:
            self.session_data_set(files_directory = files_directory)
        if owner_datafile is ...:
            owner_datafile = self.session_data.owner_datafile
        else:
            self.session_data_set(owner_datafile = owner_datafile)
        if verbose is ...:
            verbose = self.session_data.verbose
        else:
            self.session_data_set(verbose = verbose)
        # core process
        invoice_datadict = None
        self.console = __class__.console  # set a fresh Console variable usable for this method (ie, command) execution
        self.console.print(f"*** Application [red]xl2roefact[/] launched at {datetime.now()}")
        # prep Excel files to rocess as requested in command line (NOTE: if default directory does not exists will consider current directory instead)
        tmp_files_to_process = Path(files_directory)
        if not (tmp_files_to_process.exists() and tmp_files_to_process.is_dir()):
            tmp_files_to_process = Path(".").absolute()
            #FIXME prepare self.response code and text
            self.console.print(f"[dark_orange]WARNING note:[/] Default directory not found. Will consider current directory: [cyan]{tmp_files_to_process}[/].")
        if verbose:
            #FIXME prepare self.response code and text
            self.console.print(f"[yellow]INFO note:[/] files to process: [cyan]{Path(tmp_files_to_process, file_name)}[/]")
            self.console.print()
        list_of_files_to_process = list(tmp_files_to_process.glob(file_name))  # `glob()` will unify in a list with specified files as pattern
        # process Excel files list
        for a_file in list_of_files_to_process:
            rdinv_run_messages = list()  # this will collect rdinv running messages and if verbose is True will print
            invoice_to_process = Path("./", a_file)  # current file name to process, starting from current directory (the `files_directory` is already contained in)
            # prep for owner data acquiring from external data-file or from Excel
            full_path_owner_datafile = None
            if owner_datafile is not None:  # prep are to call `rdinv()` module with parameter to read supplier data from external file instead Excel
                full_path_owner_datafile = hier_get_data_file(owner_datafile)
                if not full_path_owner_datafile or full_path_owner_datafile is None:
                    # exit not having other option (continuing with Excel file is not a choice bacase supplier data from it is not guaranteed to be usable)
                    self.console.print(f"[red]ERROR: Owner data file ([cyan]{owner_datafile}[/]) is not valid or does not exists. Process terminated.[/].")
                    self.response_out(
                        status_code = 400,
                        status_text = "xl2json Owner data file is not valid or does not exists. Process terminated.",
                        status_result = None
                    )
                    return False          
            invoice_datadict = rdinv(
                invoice_type_code=invoice_type,
                file_to_process=invoice_to_process,
                debug_info=rdinv_run_messages,
                owner_datafile=full_path_owner_datafile
            )
            if verbose:
                for msg in rdinv_run_messages:
                    self.console.print(msg)
            if not invoice_datadict:
                self.console.print(f"[yellow]INFO note:[/] last step returned an empty invoice JSON and process could be incomplete. Please review previous messages.")
        # compose result before exiting
        self.response_out(
            status_code = 200,
            status_text = "xl2json command terminated",
            status_result = invoice_datadict  #TODO: extract only "Invoice" key
        )
        return True


    def response_out( #FIXME TODO: wip...@ 240527 06:00
        self, *,
        status_code = 200,
        status_text = "undefined",
        status_result = "undefined",
    ):
        """Prepare and enque a response. This is designed to be in-class used and not for public interface.
        Arguments are min of what to be enqueued. Other ibformation are constructed local.
        """
        self.response.status_code = status_code
        self.response.status_timestamp = datetime.now(timezone.utc).isoformat()
        self.response.status_text = status_text
        self.response.result = status_result
        tmp_console_plain = self.console.export_text(clear=False, styles=False)  # get console up here keeping it as plain text
        tmp_console_styled = self.console.export_html(clear=False, inline_styles=True)  # get console up here keeping it as strong styled text
        self.response.stdout_text = tmp_console_plain
        self.response.stdout_html = tmp_console_styled
        self.session_results.append(self.response)
        return


    def get_last_result(self) -> dict[CommandResult]:
        """Get last result dictionary from stack WITHOUT drooping it.

        Reeturn:
            `CommandResult`: last result as dictionary
        """
        tmp = self.session_results.pop()  # pop() method remove the item get, so ...
        self.session_results.append(tmp)  # ...put it back
        return dataclasses.asdict(tmp)


    def pop_session_results(self) -> list[CommandResult]:
        """Get all session results as dictionary.

        Reeturn:
            `CommandResult`: list with all session results as dictionary
        """
        rslt = list()
        for i in self.session_results:  # traversal is in insertion order (ie, from first to last enqueued item)
            rslt.append(dataclasses.asdict(i))
        self.session_results.clear()  # empty session results queue
        return rslt


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


