**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.1.18.dev


### 0.1.18.dev invoice customer CUI partial invoice total values calculations  (240105 h08:00)

* 240105piu_c updated `xl2roefact` package `README.md` file (with new sections for intro to Excel invoice content rules, tutorial TODO, reference to technical doc)

* 240105piu_b invoice customer search and persist for "CUI"

* 240105piu_a `rdinv.def get_excel_data_at_label(...)` changed strategy for DOWN search-method made it optional with default True (useful for Partners set-of KVs where is supposed to be or IN-LABEL or in RIGHT but NOT DOWN because there is a list of KVs not just one placed anywhere in Excel doc) TODO: this is subject of doc update

* 240103piu_d `rdinv.def get_excel_data_at_label(...)` changed strategy for IN-LABEL search-method to return all string except first word (supposed to be label) separated by space character (old strategy was to get only last work from all string)

* 240103piu_c ref invoice customer created in `config_settings.py` PATTERNs for search keys `PATTERN_FOR_PARTNER_ID` (CUI or ID), `PATTERN_FOR_PARTNER_LEGAL_NAME`

* 240103piu_b calculated item lines VAT amount as `cac_InvoiceLine.LineVatAmmount` as raw float value (not rounded to be able to round just invoice TOTAL)

* 240103piu_a `rdinv.rdinv()` updated JSON -- XML map (part of function `_build_meta_info_key(...)`)

* 240102piu_a `rdinv.rdinv()` upd & improved a clear Customer specific XML compliant structure. Targeted this XML structure:
                ```
                    <cac:PartyLegalEntity>
                        <cbc:RegistrationName>IORDANESCU PETRE PFA</cbc:RegistrationName>
                        <cbc:CompanyID>21986376</cbc:CompanyID>
                    </cac:PartyLegalEntity>
                ```

* 240101piu_a clean useless & obsolete project files, test new full build (MSI, Python wheel, documentation) ==> PASS OK

* 231229piu_a invoice customer (`<cac:AccountingCustomerParty>`) detect & set area to search for specific keys (like CUI, RegCom, IBAN, ...)
    * [x] 1. established AREA TO SEARCH for PARTNER data an `_area_to_search` (~line 244)
    * [x] 2. updated `config_settings.py` changed: (for a clear understating of constant scope, because will follow others for specific keys like: "reg com", "CUI", "bank / IBAN / cont", ...)
        - `PATTERN_FOR_INVOICE_CUSTOMER_LABEL` --> `PATTERN_FOR_INVOICE_CUSTOMER_SUBTABLE_MARKER`
        - `PATTERN_FOR_INVOICE_SUPPLIER_LABEL` --> `PATTERN_FOR_INVOICE_SUPPLIER_SUBTABLE_MARKER`
    * [x] 3. set-persist `_area_to_search` for next steps & save its key-info in associated invoice JSON (for further references) - `rdinv()` ~line 239
    * [x] 4. updated main xl2roefact README.md document ref latter changes and app structuring, concepts, ...(ideas evolving :)...
    * [x] 5. done code for `cac_AccountingSupplierParty` key by iterating full `invoice_header_area["customer_area"]` structure

* 231228piu_a improved documentation generation:
    * [x] updated all modules docstring(s) to a right markdown representation in generated documentation (ex: when use bullets THEN DO NOT indent at 1st level)
    * [x] __@IMP_NOTE:__ Changed generated documentation file to `doc/810.05a-xl2roefact_DLD_specs.md` and referred in main `doc/810.05a-xl2roefact_component.md` as this being a final solution for whole project documentation (that generated with `mkdocs`)
    * [x] updated `pyproject.toml, [tool.pdm.scripts]` table with new generated doc file name (810.05a-xl2roefact_DLD_specs.md)

* 231227piu_b updated `xl2roefact.rdinv` module ref dropped `_` chars from internal function names to allow doc generation by PyDoc until will produce a YAML file for PyDoc generator (where will be able to specify concrete list of objects regarding their names)

* 231227piu_a generated a first draft of markdown documentation:
    * [x] used Pydoc Markdown @ `https://niklasrosenstein.github.io/pydoc-markdown/usage/yaml/#yaml-example`
    * [x] results ==> `<PJ_ROOT>/xl2roefact/doc/generated_810.05a-xl2roefact_component.md`
    * [x] created PDM shell command `pdm run` (command just for quick remembers: `pydoc-markdown -I xl2roefact --render-toc >doc/generated_810.05a-xl2roefact_component.md`)

* 231226piu_b reviewed `xl2roefact` all "in use" code and updated `docstrings`

* 231226piu_a made some useful PDM scripts (ref `pyproject.toml`, table section `[tool.pdm.scripts]`) like build commands for:
    * [x] **`pdm build_wheel`** Python package,
    * [x] **`pdm build_msi`** MSI package,
    * [x] **`pdm build_all`** build all packages
    * [x] **`pdm xl2roefact`** run xl2roefact command
    * [x] updated `doc/810.05a-xl2roefact_component.md`










