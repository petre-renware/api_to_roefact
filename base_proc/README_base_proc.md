
# BASE_PROC component

This component is presented in document `.../doc_src/...110-SRE-api_to_roefact_requirements.md``






## Working directories

* __`test_data_and_specs/`__ contains test invoices: from client, a RENware one, a 3rd party one:
    * __`specs/`__ contains specification documents + `_my_notes.md` with notes & comments made in analysis phase
    * __`test_fact_*/`__ test invoices: from client, a RENware one, a 3rd party one

* ...







## Creating and deploying component

### Building Windows executable

* Change to `base-proc/` directory
* Activate environment: `.\.wenv_base_proc\Scripts\activate`
* Build the CLI version of component: `pyinstaller --onefile <source-file-name>`
* As result will be created:
    * `dist/<source-file-name>.exe` with the `Windows` executable
    * `build/<source-file-name>/` directory which will contain intermediary files usable when rebuilding CLI application
    * `<source-file-name>.spec` file with specifications used when building executable (usable when rebuilding CLI application)


>NOTE: `<source-file-name>` id normally `xls2xml.py`

