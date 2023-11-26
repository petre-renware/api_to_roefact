<!--#FIXME -[ README ]-----------------------------------------------------------------------------------------------
- when ready, this doc should become `810.05a-xl2roefact_component.md` in directory `doc_src/810-DSGN/`
- and set here a note / link to point it
-------------------------------------------------------------------------------------------------------------------->


# xl2roefact component

[TOC]

This component is presented in document `.../doc_src/...110-SRE-api_to_roefact_requirements.md``




## Detailed technical documentation

Component detailed specifications can be found at [xxx](../doc_src/810-DSGN/810.05a-xl2roefact_component.md)






## Working directories

* __`invoice_files/`__ normal directory for Excel files to be processed (here will be searched Excel files if not foud in current directory)

* ___`build/<source-file-name>/` directory which will contain intermediary files usable when rebuilding CLI application

* ___`dist/<source-file-name>.exe`___ executable generated file (format Windows x86)

* __`test_data_and_specs_originals/`__ contains test invoices: from client, a RENware one, a 3rd party one:
    * __`specs/`__ contains specification documents + `_my_notes.md` with notes & comments made in analysis phase
    * __`fact_*/`__ original test invoices: from Kraftanlagen, from RENware, from 3rd party









## Creating and deploying component

### Building Windows executable

* Change to `base-proc/` directory
* Activate environment: `.\.wenv_xl2roefact\Scripts\activate`
* Build the CLI version of component: `pyinstaller --onefile <source-file-name>`
* As result will be created:
    * `dist/<source-file-name>.exe` with the `Windows` executable
    * `build/<source-file-name>/` directory which will contain intermediary files usable when rebuilding CLI application
    * `<source-file-name>.spec` file with specifications used when building executable (usable when rebuilding CLI application)


>NOTE: `<source-file-name>` is normally `xls2xml.py`





## System modules <!--#TODO all of these specs are subject of `mkdocstrings` -->

### RDINV

Modul de procesare a fisierului format XLSX ce contine factura si colectare a datelor aferente

* Identification:
    * code-name: `rdinv`
    * copyright: (c) 2023 RENWare Software Systems
    * author: Petre Iordanescu (petre.iordanescu@gmail.com)

* Specifications:
    * document: `110-SRE-api_to_roefact_requirements.md` section `Componenta xl2roefact`
    * INTRARI: fisier format XLSX ce contine factura emisa (cod: `f-XLSX`)
    * IESIRI: fisier format JSON imagine a datelor facturii (cod: `f-JSON`)

* Components:
    - `rdinv(file_to_process: str, : str = None)`
    - `_get_merged_cells_tobe_changed(file_to_scan invoice_worksheet_name)`






### LIBUTILS

General utilities library

* Identification:
    * code-name: `libutils`
    * copyright: (c) 2023 RENWare Software Systems
    * author: Petre Iordanescu (petre.iordanescu@gmail.com)

* Components:
    - `isnumber(a_string: str) -> bool`
    - `find_str_in_list(list_of_str_to_find: list, list_to_search: list) -> int`

