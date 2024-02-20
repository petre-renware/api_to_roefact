**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.1.20.dev


### 0.1.20.dev invoice customer address (240123 h10:00)

* 240123piu_b make a full chk / review for FIXME & run `pdm build_all`

* 240123piu_a `def_inv_dir` issue ref Excel invoices default get directory, see comments in `app_cli.py` function `xl2json(...)`

* 240121piu_a updated `config_settings.py` & `rdinv.py` with constants: `PATTERN_FOR_PARTNER_REGCOM`, `PATTERN_FOR_PARTNER_IBAN`, `PATTERN_FOR_PARTNER_TEL`, `PATTERN_FOR_PARTNER_EMAIL`, `PATTERN_FOR_PARTNER_BANK`

* @CANCELED 240118_admin02 generalize a function `get_partner_info(partner_type: str "customer" | "supplier")` to get partner info with partner type as being parameter

* 240118piu_a reviewed and cleaned code: `rdinv.rdinv()`, `config_settings`, `excel_invoice_template/invoice_template_CU_tva.xlsx` (according to updates in testing used invoice)

* 240113piu_a to find `cac:PostalAddress` and write to:
    * [x] 1. right set position of key `"cac_PostalAddress"` in basic structure (invoice_header_area)
    * [x] 2a. find excel area ref customer address (...invoice_header_area...)
    * [x] 2b. disseminate & save excel original area (...invoice_header_area...)
    * [x] 3. get & set `["Invoice"]["cac_PostalAddress"]` and all is subsequent keys
    * [x] 4. update XML - JSON map for item "under" `cac_PostalAddress`
    * [x] 5. defined and included for use `DEFAULT_SUPPLIER_COUNTRY` and `DEFAULT_CUSTOMER_COUNTRY` both for "RO". Detailed desc and usage in `config_settings.py` & `rdinv.rdinv(...)`
    * [x] 6. updated invoice template for country explicit field

* 240116_admin_01 upd __version__ for 0.1.20







