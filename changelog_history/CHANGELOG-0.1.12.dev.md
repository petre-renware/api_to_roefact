**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.1.12.dev


* 231212piu_b write canonical form (as @invoice lines, see line ~122) ==> `invoice["Invoice"]["cbc_ID"]` and released `0.1.12-xl2roefact-0.1-win64.msi`

* 231212piu_a `rdinv.rdinv()` invoice header, invoice number as: `{"value": ..., "location": (row..., col...)}`

* 231211piu_b `rdinv.rdinv()` create a function special to get "one key Excel values", like invoice number or invoice issue date.  Signature:
    - `pattern_to_search_for: list[str]` - for inv number will pass the `PATTERN_FOR_INVOICE_NUMBER_LABEL`
    - `area_to_scan: list[start_cell, end_cell]` - for inv number will pass `(invoice_header_area["start_cell"], invoice_header_area["end_cell"])`
    - targeted_tye: type - what type expect (will try to convert to, if cannot will return str)

* 231211piu_a updated `config_settings.py` ref how to find it: string labels to search, direction to search effective info starting from label

* 231210piu_a localized and marked areas for invoice header (`invoice_header_area`) & invoice footer (`invoice_footer_area`) ==> dicts for header and footer with structure `{ start_cell = (row, col), end_cell = (row, col) }`


