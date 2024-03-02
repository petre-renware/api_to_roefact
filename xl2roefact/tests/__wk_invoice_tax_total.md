
# Structure

Structure to be includ as _invoice footer_ in XML format:

```xml
<cac:TaxTotal>
    <cbc:TaxAmount currencyID="RON">190.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
        <cbc:TaxableAmount currencyID="RON">1000.00</cbc:TaxableAmount>
        <cbc:TaxAmount currencyID="RON">190.00</cbc:TaxAmount>
        <cac:TaxCategory>
            <cbc:ID>S</cbc:ID>
            <cbc:Percent>19.00</cbc:Percent>
            <cac:TaxScheme>
                <cbc:ID>VAT</cbc:ID>
            </cac:TaxScheme>
        </cac:TaxCategory>
    </cac:TaxSubtotal>
</cac:TaxTotal>
```

## Calculation of items

```python

cac_TaxSubtotal = [ {
    "cbc_TaxableAmount": rounded float,  # taxable vaue, is the value where the tax will be applied, the total value w/o VAT of an item
    # ... `tmp_InvoiceLine_list["cbc_LineExtensionAmount"]` which in code is constructed before reusable parts from `Invoice` "big" dict

    "cbc_TaxAmount": rounded float,  # is the tax resulted from application on `cbc_TaxableAmount`
    # ... `LineVatAmount`

    # ...next one are just from peoduct line keys...
},
# {...},   ...another product iteration here, for prev_dict in Invoice big dict
]  # end.of `cac_TaxSubtotal`




```


# XMLGJSON map

```python

("cac_TaxTotal", "cac:TaxTotal"),
("cbc_TaxAmount", "cbc:TaxAmount"),
("cac_TaxSubtotal", "cac:TaxSubtotal"),
("cbc_TaxableAmount", "cbc:TaxableAmount"),

# NOTE: items that could already exists in map. TO CHECK.

("cac_TaxCategory", "cac:TaxCategory"),
("cbc_Percent", "cbc:Percent"),
("cbc_ID", "cbc:ID"),
("cac_TaxScheme", "cac:TaxScheme"),


```

