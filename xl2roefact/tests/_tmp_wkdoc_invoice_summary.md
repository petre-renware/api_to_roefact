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

```python

Skip to content

Code
Issues
Pull requests
run_xl2roefact_cli_app
Update rdinv.py #25
deploy
succeeded 1 minute ago in 1m 10s
Beta
Give feedback
1s
11s
2s
0s
54s
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
|                                                                             |
| D:\a\api_to_roefact\api_to_roefact\xl2roefact\xl2roefact\libutils.py:48 in  |
| dict_sum_by_key                                                             |
|                                                                             |
|    45                     except: kval = 0                                  |
|    46                     s += kval                                         |
|    47     else:                                                             |
| >  48         s += dict_sum_by_key(search_dict, sum_key)                    |
|    49     return float(s)                                                   |
|    50                                                                       |
|    51                                                                       |
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
|                                                                             |
0s
1s

RecursionError: maximum recursion depth exceeded while calling a Python object
[test-xl2roefact e4b04e1] Automated xl2roefact test-run (by RENware Software Systems)
 1 file changed, 8 insertions(+), 68 deletions(-)
To https://github.com/petre-renware/api_to_roefact
   99ed060..e4b04e1  test-xl2roefact -> test-xl2roefact

```

...EOF...