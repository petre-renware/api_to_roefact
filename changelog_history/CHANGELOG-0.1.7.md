**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.1.7

### 0.1.7 `xl2roefact.RDINV` invoice items & metadata (231126 h05:00)

* **left OPEN ISSUES in this release** [piu@231126: marked on todo plan of `0.1.8` version]
    * [x] (CLOSED@231213) _file `xl2roefact/rdinv.py`, function `__mk_kv_invoice_items_area(...)`:_ `FIXME this will be identified in `invoice_header_area` ==> should be changed accordingly`
    * [ ] --> _file `xl2roefact\invoice_files/_PLAN_model_test_factura_generat_anaf.xml`, line 114:_ `<cbc:ID>S</cbc:ID> #FIXME clarify.me_ pare a fi TIPUL PRODUSULUI: (S)erviciu sau ??? (P)rodus sau ???`


* 231126piu_a item(s) line extensions == item VAT total, item VALUE total

* 231125piu_c changed dir `excel_invoices/` with `invoice_files/`

* 231125piu_b make a plan from `__model_test_factura_generat_anaf.xml` marking TODOs & DONE tags & renaming as `_PLAN_...idem...`

* 231125piu_a final review, complete find of invoice relevant columns and write them in `invoice` dict:
    * quantity (cbc:InvoicedQuantity),
    * VAT percent (cbc:Percent),
    * description (cbc:Name),
    * uom (cbc:unitCode),
    * unit price (cbc:PriceAmount),
    * currency (c:currencyID)

* 231224piu_a FIXED VAT calculation for lines which specify a VAT as 0% - USE CASE lines for other taxes like "acciza"... - still unsolved for very simplified invoices (see code line containing text "`_vat_percent` calculation should also")

* 231123piu_c `rdinv` module, defined function `libutils.isnumber(a_string: str) -> bool` to test is a string is valid as any kind of number

* 231123piu_b `rdinv` module, function to search for a list of string in a list items (suitable to identify useful / relevant invoice columns from Excel format) ==> **`__find_str_in_list(str_to_find: str, list_to_search: list)`**

* 231123piu_a prepared function `__mk_kv_invoice_items_area(...)` to transform `invoice_items_area` in "canonical JSON format" (as kv pairs)

* 231122piu_a  `invoice_items_area` & `meta_info` review, check and clean code

* 231121piu_a final `invoice` dict / JSON data: moved all effective data under key `"excel_data"` (preparing so for final storable invoice "real keys")

* 231119piu_b `invoice_items_area` set unknown rows header to `<current line number>.NOTE-<seq>`, where `seq` is an ordered sequence of letters (ie, resulting something like: `1.a, 1.b, ...`)
\* 231119piu_a closed:
    * [x] invoice `meta_info` area
    * [x] a more defined, clean & clear `invoice_items_area`
    * [x] add `last_processing_UTCtime` in `meta_info` dictionary
    * [x] written `invoice` dict to a JSON (`f-JSON` file, see doc: `https://apitoroefact.renware.eu/commercial_agreement/110-SRE-api_to_roefact_requirements.html#vedere-de-ansamblu-a-solutiei`)

* 231112piu_a refactor:
    *  [x] `base_proc` to `xl2roefact`
    *  [x] `BASE_PROC` to `xl2roefact`
    *  [x] update documentation
    *  [x] publish site

* 231109piu_a installed module `pylightxl` in base environment (ie, in project root) to allow modules calling from root for future web components & updated requirements.txt

* 231108piu_f RDINV (`rdinv.py`) secure for "unwanted crashes" errors (missing info) & clean code

* 2811080iu_e install `mkdocstrings`, update `mkdocs.yml` and create a markdown document for xl2roefact component (did) not succeeded search for 'FIXME temporary disabled because errs' ...longer_string_...

* 231108piu_d documented that `XLSX` is the only Excel file format supported (in `110-SRE-api_to_roefact_requirements.md`) & published site

* 231108piu_c xl2roefact (`xl2roefact.py`) transformed in class & parametrized worksheet name containing invoice ==> **class BaseProc()**

* 231108piu_b RDINV (`rdinv.py`) module set directories environment & open invoice

* 231108piu_a consolidate decomposition (from `231107piu_c`) ==> directory `.../xl2roefact/modules/`

* 231107piu_c transform decomposition (from `231107piu_b`) into complete Python modules (making directories for each)

* 231107piu_b created module files according to decomposition (specs doc `110-SRE-api_to_roefact_requirements.md`)

* 230107piu_a made a first DRAFT runnable CLI program with `Typer` (`https://typer.tiangolo.com/`) from `xls2xml.py` ==> `dist/xls2xml.exe`



