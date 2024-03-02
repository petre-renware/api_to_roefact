
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

cbc_TaxableAmount: float = ...

cbc_TaxAmount




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

