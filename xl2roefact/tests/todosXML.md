

# XML tags to be implemented


```xml
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
... upper tag included to see level of todo tags ...


    <cbc:DueDate>2023-11-21</cbc:DueDate>  #TODO tbd... - acesta est edata scadentei - planned for application version 2.x.x
    <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>  #TODO tbd... # this must remain as is here and check also `factura_facuta_in_anaf_sintaxa_UBL_20231128.xml` (380 value means == NORMAL INVOICE, not credit note, return invoice, canceling invoice, ...)
    <cbc:Note>test generat 2023-11-21</cbc:Note>  #TODO tbd...
    <cbc:TaxPointDate>2013-11-20</cbc:TaxPointDate>  #TODO tbd...

    <cac:Delivery>  #TODO tbd...  #NOTE ? do not know if simple Excel processing can give this info - NEEED ERP
        <cbc:ActualDeliveryDate>2023-11-19</cbc:ActualDeliveryDate>
    </cac:Delivery>

    <cac:PaymentMeans>  #TODO tbd...   #NOTE ? do not know if simple Excel processing can give this info - NEEED ERP
        <cbc:PaymentMeansCode>1</cbc:PaymentMeansCode>
    </cac:PaymentMeans>


</Invoice>
```



# JSON-XML map


```python

[
"cbc_DueDate",
"cbc:DueDate"]

[
"cbc_InvoiceTypeCode",
"cbc:InvoiceTypeCode"]

[
"cbc_Note",
"cbc:Note"]

[
"cbc_TaxPointDate",
"cbc:TaxPointDate"]

[
"cac_Delivery",
"cac:Delivery"]

[
"cbc_ActualDeliveryDate",
"cbc:ActualDeliveryDate"]

[
"cac_PaymentMeans",
"cac:PaymentMeans"]

[
"cbc_PaymentMeansCode",
"cbc:PaymentMeansCode"]

```

