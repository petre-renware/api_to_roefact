# Generated invoice JSON model

>NOTE: ***The following model should be considered ONLY for JSON keys. All data is just sample / not real just for a better understanding of its format (or "how it looks like").***


```json
{
    "Invoice": {
        "cbc_ID": "INV-001",
        "cbc_DocumentCurrencyCode": "RON",
        "cbc_IssueDate": "2023-08-28",
        "cac_AccountingCustomerParty": {
            "cac:Party": {
                "cac_PartyLegalEntity": {
                    "cbc_CompanyID": "17753763",
                    "cbc_RegistrationName": "SOME COMPANY SRL"
                },
                "cac_PostalAddress": {
                    "cbc_StreetName": "",
                    "cbc_CityName": "Bucureşti Sectorul 1, Strada: Rozelor, Nr. 21, Etaj parter, tara: Romania",
                    "cbc_PostalZone": "5555544",
                    "cac_Country": {
                        "cbc_IdentificationCode": "RO"
                    }
                },
                "cac_Contact": {
                    "cbc_Telephone": "...",
                    "cbc_ElectronicMail": "...",
                    "RegCom": "J40/.../...",
                    "Bank": "BCR Ag Sala Palatului",
                    "IBAN": "ROxx RNCB ... ... ... ..."
                }
            }
        },
        "cac_InvoiceLine": [
            {
                "cbc_ID": "1",
                "cbc_InvoicedQuantity": 3.5,
                "cbc_unitCode": "buc",
                "cac_Item": {
                    "cbc_Name": "Product x name here",
                    "cac_ClassifiedTaxCategory": {
                        "cbc_Percent": 0.19,
                        "cac_TaxScheme": {
                            "cbc_ID": "VAT"
                        }
                    }
                },
                "cac_Price": {
                    "cbc_PriceAmount": 11111.5,
                    "cbc_currencyID": "RON"
                },
                "cbc_LineExtensionAmount": 38890.25,
                "LineVatAmount": 7389.1475
            },
            {
                "cbc_ID": "1.NOTE-a",
                "cbc_InvoicedQuantity": null,
                "cbc_unitCode": null,
                "cac_Item": {
                    "cbc_Name": "just some supplementary explanations ref first product...",
                    "cac_ClassifiedTaxCategory": {
                        "cbc_Percent": null,
                        "cac_TaxScheme": {
                            "cbc_ID": null
                        }
                    }
                },
                "cac_Price": {
                    "cbc_PriceAmount": null,
                    "cbc_currencyID": null
                },
                "cbc_LineExtensionAmount": null,
                "LineVatAmount": null
            },
            {
                "cbc_ID": "1.NOTE-b",
                "cbc_InvoicedQuantity": null,
                "cbc_unitCode": null,
                "cac_Item": {
                    "cbc_Name": "another explanations line...",
                    "cac_ClassifiedTaxCategory": {
                        "cbc_Percent": null,
                        "cac_TaxScheme": {
                            "cbc_ID": null
                        }
                    }
                },
                "cac_Price": {
                    "cbc_PriceAmount": null,
                    "cbc_currencyID": null
                },
                "cbc_LineExtensionAmount": null,
                "LineVatAmount": null
            },
            {
                "cbc_ID": "1.NOTE-c",
                "cbc_InvoicedQuantity": null,
                "cbc_unitCode": null,
                "cac_Item": {
                    "cbc_Name": "'*** a comment ref price xchg rate 3000EUR ref BNR",
                    "cac_ClassifiedTaxCategory": {
                        "cbc_Percent": null,
                        "cac_TaxScheme": {
                            "cbc_ID": null
                        }
                    }
                },
                "cac_Price": {
                    "cbc_PriceAmount": null,
                    "cbc_currencyID": null
                },
                "cbc_LineExtensionAmount": null,
                "LineVatAmount": null
            },
            {
                "cbc_ID": "2",
                "cbc_InvoicedQuantity": 1,
                "cbc_unitCode": "",
                "cac_Item": {
                    "cbc_Name": "Acciza 1%",
                    "cac_ClassifiedTaxCategory": {
                        "cbc_Percent": null,
                        "cac_TaxScheme": {
                            "cbc_ID": null
                        }
                    }
                },
                "cac_Price": {
                    "cbc_PriceAmount": 111.115,
                    "cbc_currencyID": "RON"
                },
                "cbc_LineExtensionAmount": 111.11,
                "LineVatAmount": 0.0
            }
        ],
        "cac_LegalMonetaryTotal": {
            "cbc_LineExtensionAmount": 39001.0,
            "cbc_TaxExclusiveAmount": 39001.0,
            "cbc_TaxInclusiveAmount": 46390.0,
            "cbc_PayableAmount": 46390.0
        },
        "cac_TaxTotal": {
            "cbc_TaxAmount": 7389.15,
            "cac_TaxSubtotal": [
                {
                    "cbc_TaxableAmount": 38890.25,
                    "cbc_TaxAmount": 7389.15,
                    "cac_TaxCategory": {
                        "cac_ClassifiedTaxCategory": {
                            "cbc_Percent": 0.19,
                            "cac_TaxScheme": {
                                "cbc_ID": "VAT"
                            }
                        },
                        "ID": "S"
                    }
                },
                {
                    "cbc_TaxableAmount": null,
                    "cbc_TaxAmount": null,
                    "cac_TaxCategory": {
                        "cac_ClassifiedTaxCategory": {
                            "cbc_Percent": null,
                            "cac_TaxScheme": {
                                "cbc_ID": null
                            }
                        },
                        "ID": "S"
                    }
                }
            ]
        },
    },
    "meta_info": {
        "file": "invoice_json_model_.xlsx",
        "file_CRC": "...file CRC (uniquely identify the invoice file used)",
        "last_processing_time": "2021-01-23T07:39:30.115329+00:00",
        "invoice_worksheet": "FACTURA",
        "invoice_max_rows": 31,
        "invoice_max_cols": 9,
        "items_table_start_marker": "#",
        "items_table_start_cell": [
            20,
            1
        ],
        "invoice_XML_schemes": {
            "xmlns": "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2",
            "xmlns:cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "xmlns:cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "xmlns:ns4": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
            "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
            "xsi:schemaLocation": "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2 http://docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd"
        },
        "map_JSONkeys_XMLtags": [
            [
                "cac_InvoiceLine",
                "cac:InvoiceLine"
            ],
            [
                "cac_Item",
                "cac:Item"
            ],
            [
                "cac_ClassifiedTaxCategory",
                "cac:ClassifiedTaxCategory"
            ],
            [
                "cac_TaxScheme",
                "cac:TaxScheme"
            ],
            [
                "cac_Price",
                "cac:Price"
            ],
            [
                "cbc_ID",
                "cbc:ID"
            ],
            [
                "cbc_InvoicedQuantity",
                "cbc:InvoicedQuantity"
            ],
            [
                "cbc_unitCode",
                "cbc:unitCode"
            ],
            [
                "cbc_Name",
                "cbc:Name"
            ],
            [
                "cbc_Percent",
                "cbc:Percent"
            ],
            [
                "cbc_PriceAmount",
                "cbc:PriceAmount"
            ],
            [
                "cbc_currencyID",
                "cbc:currencyID"
            ],
            [
                "cbc_LineExtensionAmount",
                "cbc:LineExtensionAmount"
            ],
            [
                "cbc_ID",
                "cbc:ID"
            ],
            [
                "cbc_DocumentCurrencyCode",
                "cbc:DocumentCurrencyCode"
            ],
            [
                "cbc_IssueDate",
                "cbc:IssueDate"
            ],
            [
                "cac_AccountingCustomerParty",
                "cac:AccountingCustomerParty"
            ],
            [
                "cac_Party",
                "cac:Party"
            ],
            [
                "cac_PartyLegalEntity",
                "cac:PartyLegalEntity"
            ],
            [
                "cbc_CompanyID",
                "cbc:CompanyID"
            ],
            [
                "cbc_RegistrationName",
                "cbc:RegistrationName"
            ],
            [
                "cac_PostalAddress",
                "cac:PostalAddress"
            ],
            [
                "cbc_StreetName",
                "cbc:StreetName"
            ],
            [
                "cbc_CityName",
                "cbc:CityName"
            ],
            [
                "cbc_PostalZone",
                "cbc:PostalZone"
            ],
            [
                "cac_Country",
                "cac:Country"
            ],
            [
                "cbc_IdentificationCode",
                "cbc:IdentificationCode"
            ]
        ]
    },
    "excel_original_data": {
        "invoice_items_area": {
            "keyrows": [
                1,
                "1.NOTE-a",
                "1.NOTE-b",
                "1.NOTE-c",
                2
            ],
            "keycols": [
                "Denumire produse sau servicii",
                "UM",
                "Cant",
                "Pret unitar",
                "Valoare fara TVA",
                "Cota TVA",
                "Valoare TVA"
            ],
            "data": [
                [
                    "...excel data...",
                    "buc",
                    3.5,
                    11111.5,
                    38890.25,
                    0.19,
                    7389.15
                ],
                [
                    "...excel data...",
                    "",
                    "",
                    "",
                    "",
                    "",
                    ""
                ],
                [
                    ...excel data...",
                    "",
                    "",
                    "",
                    "",
                    "",
                    ""
                ],
                [
                    "'*** a comment ref price xchg rate 3000EUR ref BNR",
                    "",
                    "",
                    "",
                    "",
                    "",
                    ""
                ],
                [
                    "Acciza 1%",
                    "",
                    1,
                    111.115,
                    111.12,
                    "",
                    0
                ]
            ]
        },
        "invoice_header_area": {
            "start_cell": [
                1,
                1
            ],
            "end_cell": [
                19,
                9
            ],
            "invoice_number": {
                "value": "INV-001",
                "location": [
                    5,
                    3
                ],
                "label_value": "Numar factura:",
                "label_location": [
                    5,
                    2
                ]
            },
            "issued_date": {
                "value": "2021-08-28",
                "location": [
                    6,
                    3
                ],
                "label_value": "Data:",
                "label_location": [
                    6,
                    2
                ]
            },
            "currency": {
                "value": "RON",
                "location": [
                    6,
                    9
                ],
                "label_value": "Moneda:",
                "label_location": [
                    6,
                    8
                ]
            },
            "customer_area": {
                "area_info": {
                    "value": "Client",
                    "location": [
                        [
                            8,
                            5
                        ],
                        [
                            17,
                            6
                        ]
                    ]
                },
                "CUI": {
                    "value": "...exceel data...",
                    "location": [
                        11,
                        6
                    ],
                    "label_value": "CIF:",
                    "label_location": [
                        11,
                        5
                    ]
                },
                "RegistrationName": {
                    "value": "SOME COMPANY SRL",
                    "location": [
                        9,
                        5
                    ],
                    "label_value": "n/a",
                    "label_location": "n/a"
                },
                "PostalAddress": {
                    "cbc_StreetName": "",
                    "cbc_CityName": "...excel data...",
                    "cbc_PostalZone": "",
                    "cac_Country": {
                        "cbc_IdentificationCode": "RO"
                    }
                }
            },
            "supplier_area": "...future..."
        },
        "invoice_footer_area": {
            "start_cell": [
                26,
                1
            ],
            "end_cell": [
                31,
                9
            ]
        }
    }
}
```

