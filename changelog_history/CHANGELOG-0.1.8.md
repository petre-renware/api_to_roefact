**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.1.8

### 0.1.8 improved application structure and first executable release (231201 h07:30)

* 231201piu_b installed `cx-Freeze` library and build a new Windows executable, update documentation - need future improvement to make `msi` package, but TEST PASSED and works perfectly

* 231201piu_a improve CLI application structure (`xl2roefact.py`) and commands: `xl2json`, `about`

* 231130piu_a `xl2roefact.py`, `——excel_files_directory`: option, make it of type pathlib.Path, dealut remain as is, validators; is dir, exists, writable, readable, resolve_path

* 231129piu_b updated `xl2roefact.py` (main application) changed command `run` --> `xl2json` and add parameter `excel_files_directory` (future intention is to make commands: `xl2json - RDINV`, `json2xml - WRXML`, `json2pdf`, `xml2roefact - LDXML`)

* 231129piu_a adopted new REN invoice template (test with data from RENF-1004)

* 231128piu_b made `config_settings.py` for general application configuration purposes and an application command (`xl2roefact settings`) to print them

* 231128piu_a made `xl2roefact.py` (main library file) as CLI executable structure (with `Typer` library)

* 231127piu_c introduced **key `Invoice`** in  invoice JSON generated structure (also representing the "entity" in XML representation)

* 231127piu_b module `rdinv` crated a distinct function for building of `meta_info` key (main `invoice` dictionary)

* 231127piu_a created in invoice JSON map JSON key --> XML property (`meta_info["map_JSONkeys_XMLtags"]`) as `list of tuple(JSONkey: str, XMLtag: str)`

* 231127piu_a created draft data models for: invoice (exportable as JSON and XML) and other entities (owner, customer) ==> `data_models.py`

