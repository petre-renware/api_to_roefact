
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

### Items "in scope" and as dict desired structure

```python
cac_TaxTotal = {
    "cbc_TaxAmount": round(sum(cac_TaxSubtotal, 2),  #NOTE it is a summarization of next item which is a list (a detailed presentation of info)
    "cac_TaxSubtotal" = [{
        "cbc_TaxableAmount": rounded float,  # taxable value, is the value where the tax will be applied, the total value w/o VAT of an item
        "cbc_TaxAmount": rounded float,  # is the tax resulted from application on `cbc_TaxableAmount` === `LineVatAmount`
        # ... and next keys are just from peoduct line keys...
    },
    {...},  # ...another product iteration here, for prev_dict in Invoice big dict
]
#NOTE attn DON'T close last list line with comma `,`

}
```


### detaild specs calculation as "SQL view"

>NOTE: code must constructed before "rdinv() reusable parts" dict because in use temporary extracted items list from whole Ivoice dict structure.

```sql

SELECT
    cbc_TaxableAmount as
        SUM(tmp_InvoiceLine_list["cbc_LineExtensionAmount"])
    cbc_TaxAmount as
        SUM(tmp_InvoiceLine_list["LineVatAmount"])
WHERE
    tmp_InvoiceLine_list["cac_Item"]["cac_ClassifiedTaxCategory"]["cbc_Percent"]["cac_TaxScheme"]["cbc_ID"] == "VAT"
GROUP BY
    tmp_InvoiceLine_list["cac_Item"]["cac_ClassifiedTaxCategory"]["cbc_Percent"]

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

