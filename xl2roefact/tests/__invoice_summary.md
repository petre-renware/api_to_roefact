




```xml
                <cac:LegalMonetaryTotal>
                    <cbc:LineExtensionAmount currencyID="RON">1000.00</cbc:LineExtensionAmount>
                        -NOTE SUM(`cac_InvoiceLine.cbc_LineExtensionAmount`)
                    <cbc:TaxExclusiveAmount currencyID="RON">1000.00</cbc:TaxExclusiveAmount>
                        -NOTE: SUM(`cac_InvoiceLine.cbc_LineExtensionAmount`)  NOTE-[piu@240103] nu m-am prins inca care-i diferenta fata de item anterior, pentru ca aici este totalul mare al facturii...
                    <cbc:TaxInclusiveAmount currencyID="RON">1190.00</cbc:TaxInclusiveAmount>
                        -NOTE: SUM(`cac_InvoiceLine.cbc_LineExtensionAmount` + `cac_InvoiceLine.LineVatAmount`)
                    <cbc:PayableAmount currencyID="RON">1190.00</cbc:PayableAmount>
                        -NOTE: SUM(`cac_InvoiceLine.cbc_LineExtensionAmount` + `cac_InvoiceLine.LineVatAmount`)  NOTE-[piu@240103] nu m-am prins inca care-i diferenta fata de item anterior, pentru ca aici este totalul mare al facturii...
                </cac:LegalMonetaryTotal>
            - NOTE-IMPORTANT-NOTE: only TOTALIZED values need to be rounded 2 decimals (because LineVatAmount is let raw calculation to ve able to round here after SUM)
            - NOTE: TOTAL invoice VAT can be obtained as `SUM(from existing key cac_InvoiceLine.LineVatAmount`) adding lines VAT
```





