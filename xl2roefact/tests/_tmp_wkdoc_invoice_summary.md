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

...


```

...EOF...