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



## run @240223 05:40

```python




Code
Issues
Pull requests
run_xl2roefact_cli_app
Update _tmp_wkdoc_invoice_summary.md #27
deploy
succeeded 1 minute ago in 1m 11s
Beta
Give feedback
1s
10s
1s
0s
57s
| |                                             'cbc_ID': '1',              | |
| |                                             'cbc_InvoicedQuantity': 1,  | |
| |                                             'cbc_unitCode': None,       | |
| |                                             'cac_Item': {               | |
| |                                                 'cbc_Name': 'Inlocuit   | |
| |                                     conducta PSI coloana C2 DAV.',      | |
| |                                                 'cac_ClassifiedTaxCate� | |
| |                                     {                                   | |
| |                                                     'cbc_Percent':      | |
| |                                     0.19,                               | |
| |                                                     'cac_TaxScheme': {  | |
| |                                                         'cbc_ID': 'VAT' | |
| |                                                     }                   | |
| |                                                 }                       | |
| |                                             },                          | |
| |                                             'cac_Price': {              | |
| |                                                 'cbc_PriceAmount':      | |
| |                                     42756.08,                           | |
| |                                                 'cbc_currencyID': 'RON' | |
| |                                             },                          | |
| |                                             'cbc_LineExtensionAmount':  | |
| |                                     42756.08,                           | |
| |                                             'LineVatAmount': 8123.6552  | |
| |                                         },                              | |
| |                                     )                                   | |
| |                        ulc_footer = (34, 1)                             | |
| |                        ulc_header = (1, 1)                              | |
| |                                ws = pylightxl.Database.Worksheet        | |
| +-------------------------------------------------------------------------+ |
|                                                                             |
| D:\a\api_to_roefact\api_to_roefact\xl2roefact\xl2roefact\libutils.py:48 in  |
| dict_sum_by_key                                                             |
|                                                                             |
|    45                     except: kval = 0                                  |
|    46                     s += kval                                         |
|    47     else:                                                             |
| >  48         if isinstance(search_dict[k], dict):                          |
|    49             s += dict_sum_by_key(search_dict[k], sum_key)             |
|    50         if k == sum_key:                                              |
|    51             try: kval = int(search_dict[k])                           |
|                                                                             |
| +-------------------------------- locals ---------------------------------+ |
| |           s = 0                                                         | |
| | search_dict = (                                                         | |
| |                   {                                                     | |
| |                       'cbc_ID': '1',                                    | |
| |                       'cbc_InvoicedQuantity': 1,                        | |
| |                       'cbc_unitCode': None,                             | |
| |                       'cac_Item': {                                     | |
| |                           'cbc_Name': 'Inlocuit conducta PSI coloana C2 | |
| |               DAV.',                                                    | |
| |                           'cac_ClassifiedTaxCategory': {                | |
| |                               'cbc_Percent': 0.19,                      | |
| |                               'cac_TaxScheme': {'cbc_ID': 'VAT'}        | |
| |                           }                                             | |
| |                       },                                                | |
| |                       'cac_Price': {                                    | |
| |                           'cbc_PriceAmount': 42756.08,                  | |
| |                           'cbc_currencyID': 'RON'                       | |
| |                       },                                                | |
| |                       'cbc_LineExtensionAmount': 42756.08,              | |
| |                       'LineVatAmount': 8123.6552                        | |
| |                   },                                                    | |
| |               )                                                         | |
| |     sum_key = 'cbc_LineExtensionAmount'                                 | |
| +-------------------------------------------------------------------------+ |
+-----------------------------------------------------------------------------+
UnboundLocalError: local variable 'k' referenced before assignment
[test-xl2roefact cedaf7f] Automated xl2roefact test-run (by RENware Software Systems)


UnboundLocalError: local variable 'k' referenced before assignment
[test-xl2roefact cedaf7f] Automated xl2roefact test-run (by RENware Software Systems)
 1 file changed, 2 insertions(+), 2 deletions(-)
To https://github.com/petre-renware/api_to_roefact
   4418fec..cedaf7f  test-xl2roefact -> test-xl2roefact

```

...EOF...