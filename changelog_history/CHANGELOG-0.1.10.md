**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.1.10

### 0.1.10 command interface improved, `msi` package building, invoice template & updated documentation (231207 h12:00)

* 231207piu_b build a `MSI` package for `0.1.10` version ==> **`0.1.10-xl2roefact-0.1-win64.msi`**, also installed `Python 3.11` + `cx-Freeze` & updated `requirements_xl2roefact.txt`

* 231207piu_a FIXED errors due to Excel files directory duplication in `xl2roefact` & `rdinv()`

* 231206piu_a clean code for `rdinv` & `xl2roefact`, reviewed cnd closed some open issues (todos, notes, ...)

* 231205piu_b made a directory for INVOICE TEMPLATE (`excel_invoice_template/`) to be delivered with solutions "for who need a simple template", also write here a `README_excel_invoice_rules.md` to describe all required conditions in order to be "RECOGNIZED & TRANSLATED to JSON"

* 231205piu_a change all solution to use `rich` library instead of `colorama` (Rich library ref `https://rich.readthedocs.io/en/stable/index.html`)
    * [x] drop all `from colorama import Fore, Back, Style`
    * [x] add new `from rich import print`
    * [x] update all places where `{Fore....}` with `[...]` as:
        * [x] `{Fore.YELLOW}` with `[yellow]`
        * [x] `{Fore.GREEN}` with `[green]`
        * [x] `{Fore.MAGENTA}` with `[magenta]`
        * [x] `{Fore.BLUE}` with `[blue]`
        * [x] `{Fore.CYAN}` with `[cyan]`
        * [x] `{Fore.RED}` with `[red]`
    * [x] change all `typer.echo` with `print`
    * [x] update all places where `{Style.RESET_ALL}` with `[/]`

* 231204piu_c build new executable and installer ==> `dist/0.1.10.231204piu_a-xl2roefact-0.1-win64.msi`

* 231204piu_b created `./doc/` renamed and moved all documentation documents - intention to keep clean `xl2roefact root`

* 231204piu_a `xl2roefact xl2json` check rdinv() result and if return False, ONLY print a message of "INFO note" then continue with next file (the effective error was print by module itself) && build a new executable package ==> `dist/0.1.10.231204piu_a-exe.win-amd64-3.10.zip`


