# invoice summary structure

* place: tdinv.py lin 442
* note text; TOTAL_invoice_strucuture (NOTE: refered by line "TODO: need  to contsruct TOTAL invoice structure ...", line ~>= 314)




```xml
<cac:LegalMonetaryTotal>

  <cbc:LineExtensionAmount currencyID="RON">1000.00</cbc:LineExtensionAmount>
    -NOTE ROUND...SUM(`cac_InvoiceLine.cbc_LineExtensionAmount`)

  <cbc:TaxExclusiveAmount currencyID="RON">1000.00</cbc:TaxExclusiveAmount>
    -NOTE: ROUND...SUM(`cac_InvoiceLine.cbc_LineExtensionAmount`)
    -NOTE-[piu@240103] nu m-am prins inca care-i diferenta fata de item anterior, pentru ca aici este totalul mare al facturii...

  <cbc:TaxInclusiveAmount currencyID="RON">1190.00</cbc:TaxInclusiveAmount>
    -NOTE: ROUND...SUM(`cac_InvoiceLine.cbc_LineExtensionAmount` + `cac_InvoiceLine.LineVatAmount`)

  <cbc:PayableAmount currencyID="RON">1190.00</cbc:PayableAmount>
    -NOTE: ROUND...SUM(`cac_InvoiceLine.cbc_LineExtensionAmount` + `cac_InvoiceLine.LineVatAmount`)
    =NOTE-[piu@240103] nu m-am prins inca care-i diferenta fata de item anterior, pentru ca aici este totalul mare al facturii...

</cac:LegalMonetaryTotal>


... existing info ...
<cac:InvoiceLine>...</cac:InvoiceLine>
...

```





## Map to be created

```python
[
    #... previous code here

    ("cac_LegalMonetaryTotal", "cac:LegalMonetaryTotal"),
    ("cbc_LineExtensionAmount", "cbc:LineExtensionAmount"),
    ("cbc_TaxExclusiveAmount", "cbc:TaxExclusiveAmount"),
    ("cbc_TaxInclusiveAmount", "cbc:TaxInclusiveAmount",),
    ("cbc_PayableAmount", "cbc:PayableAmount"),

    #... not needed from here
]
```



## run @240223 05:10

```
Skip to content

Code
Issues
Pull requests
run_xl2roefact_cli_app
Update _test_results.txt #26
deploy
succeeded 1 minute ago in 1m 2s
Beta
Give feedback
1s
11s
1s
0s
45s
| |          files_directory = WindowsPath('D:/a/api_to_roefact/api_to_roe� | |
| |       invoice_to_process = WindowsPath('D:/a/api_to_roefact/api_to_roe� | |
| | list_of_files_to_process = [                                            | |
| |                                WindowsPath('D:/a/api_to_roefact/api_to� | |
| |                                WindowsPath('D:/a/api_to_roefact/api_to� | |
| |                            ]                                            | |
| |     tmp_files_to_process = WindowsPath('D:/a/api_to_roefact/api_to_roe� | |
| |                  verbose = False                                        | |
| +-------------------------------------------------------------------------+ |
|                                                                             |
| D:\a\api_to_roefact\api_to_roefact\xl2roefact\xl2roefact\rdinv.py:409 in    |
| rdinv                                                                       |
|                                                                             |
|   406                                                                       |
|   407             #FIXME: ...hereuare... after finish `invoice_header_area` |
|   408             "cac_LegalMonetaryTotal": {                               |
| > 409                 "cbc_LineExtensionAmount": round(dict_sum_by_key(tmp_ |
|   410                 "cbc_TaxExclusiveAmount": "...",  #  ROUND...SUM   (` |
|   411                 "cbc_TaxInclusiveAmount": "...",  #  ROUND...SUM   (` |
|   412                 "cbc_PayableAmount": "...",  #       ROUND...SUM   (` |
|                                                                             |
| +-------------------------------- locals ---------------------------------+ |
| |                   _area_to_search = ((8, 2), (18, 3))                   | |
| |          _area_to_search_end_cell = [18, 3]                             | |
| |        _area_to_search_start_cell = [8, 2]                              | |
| |                         _cell_col = 3                                   | |
| |                       _cell_index = (32, 3)                             | |
| |                         _cell_row = 32                                  | |
| |             _crt_scanned_cell_idx = (19, 2)                             | |
| |             _crt_scanned_cell_val = ''                                  | |
| | _found_cell_for_invoice_items_area� (29, 1, 'No. crt.')                 | |
| |                                   =                                     | |
| |                 _last_ok_position = (18, 2)                             | |
| |  _location_of_header_partner_area = (8, 2)                              | |
| |          _location_of_value_found = (9, 2)                              | |
| |                   _start_cell_val = ''                                  | |
| |                  _temp_found_data = {                                   | |
| |                                         'value': 'Coralilor Nr. 22',    | |
| |                                         'location': (12, 2),            | |
| |                                         'label_value': 'Str. Coralilor  | |
| |                                     Nr. 22',                            | |
| |                                         'label_location': (12, 2)       | |
| |                                     }                                   | |
| |                         _tmp_bank = {                                   | |
| |                                         'value': 'Comerciala Romana',   | |
| |                                         'location': (16, 2),            | |
| |                                         'label_value': 'Banca           | |
| |                                     Comerciala Romana',                 | |
| |                                         'label_location': (16, 2)       | |
| |                                     }                                   | |
0s
1s
0s


```

