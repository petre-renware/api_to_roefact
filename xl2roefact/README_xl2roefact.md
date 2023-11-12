<!--#FIXME -[ README ]-----------------------------------------------------------------------------------------------
- when ready, this doc should become `810.05a-xl2roefact_component.md` in directory `doc_src/810-DSGN/`
- and set here a note / link to point it
-------------------------------------------------------------------------------------------------------------------->


# xl2roefact component

This component is presented in document `.../doc_src/...110-SRE-api_to_roefact_requirements.md``




## Detailed technical documentation

Component detailed specifications can be found at [xxx](../doc_src/810-DSGN/810.05a-xl2roefact_component.md)






## Working directories

* __`test_data_and_specs/`__ contains test invoices: from client, a RENware one, a 3rd party one:
    * __`specs/`__ contains specification documents + `_my_notes.md` with notes & comments made in analysis phase
    * __`test_fact_*/`__ test invoices: from client, a RENware one, a 3rd party one

* ___`build/<source-file-name>/` directory which will contain intermediary files usable when rebuilding CLI application

* ___`dist/<source-file-name>.exe`___ executable generated file (format Windows x86)







## Creating and deploying component

### Building Windows executable

* Change to `base-proc/` directory
* Activate environment: `.\.wenv_xl2roefact\Scripts\activate`
* Build the CLI version of component: `pyinstaller --onefile <source-file-name>`
* As result will be created:
    * `dist/<source-file-name>.exe` with the `Windows` executable
    * `build/<source-file-name>/` directory which will contain intermediary files usable when rebuilding CLI application
    * `<source-file-name>.spec` file with specifications used when building executable (usable when rebuilding CLI application)


>NOTE: `<source-file-name>` id normally `xls2xml.py`





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

    * `rdinv(file_to_process: str, invoice_data_worksheet: str = None)`
    main function of RDINV module
    - Arguments:
        - `file_to_process`: the invoice file (exact file with path)
        - `invoice_data_worksheet`: the worksheet containing invoice
    - Return:
        - tuple of `(invoice_header_area, invoice_lines_area, invoice_footer_area)`


    * `_get_merged_cells_tobe_changed(file_to_scan, invoice_worksheet_name)`
    scan Excel file to detect all merged ranges
    - Identification:
        - code-name: `_get_merged_cells_tobe_changed`
        - copyright: (c) 2023 RENWare Software Systems
        - author: Petre Iordanescu (petre.iordanescu@gmail.com)
    - Arguments:
        - `file_to_scan`: the excel file to be scanned
        - `invoice_worksheet_name`: the worksheet to be scanned
        - `only_cells_tobe_changed`: boolean indicating to
    - Return:
        - cells_to_be_changed: list ONLY with cells that need to be chaged (ie, filled with string SYS_FILLED_EMPTY_CELL)
    - Notes:
        - function is intended to be used ONLY internal in this module
        - use `openpyxl` library to do its job




