
# Structure

Structure to be includ as _invoice footer_ in XML format:

```xml
<cac:TaxTotal>  #TODO tbd...
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



# XMLGJSON map

```python
{ 

("xxx", "cac:TaxTotal"),
("xxx", "cbc:TaxAmount"),
("xxx", "cac:TaxSubtotal"),
("xxx", "cbc:TaxableAmount"),

# NOTE: items that could already exists in map. TO CHECK.

("xxx", "cac:TaxCategory"),
("xxx", "cbc:Percent"),
("xxx", "cbc:ID"),
("xxx", "cac:TaxScheme"),


... }  #FIXME ignore.me
```

