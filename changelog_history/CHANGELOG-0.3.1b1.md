**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.3.1b1

### 0.3.1b1 fixed bug JSON->["Invoice"]["cac_InvoiceLine"] list[list] (230306 h19:30)

???+ info "Release versions"
    * xl2roefact: "0.3.1b1"
    * web2roefact: "n/a"
    * invoice_template: "0.1.20"
    * INVOICEtoROefact: "0.3.1b1"

* `230406piu07` release version:
     * [x] 1. update xl2roefact version
     * [x] 2. build new app
     * [x] 3. update downloads.md doc
     * [x] 3. build site
     * [x] 4. publish on PyPi
* `230406piu06` FIXED `240306piu05` ref JSON->["Invoice"]["cac_InvoiceLine"] list[list] bug by transforming in 1-dimensional list using strategy from `TO FIX -> item 3`. TEST PASS.
* `240306piu05` TEST POINT: converted online the invoice JSON file to XML ==> `Fact_Petrom_11017969.xml`. **RESOLUTIONS:**
    * ATTN: the usable part is strict those related to "Invoice" key, any other information is not relevant and will not be included in application generated XML
    * TO FIX: JSON generated key "cac_InvoiceLine" is list[list] the first list being obsolete (just item 0 which is the effective list). Proposals:
        * 1. at XML generation to preserve only `cac_InvoiceLine[0]` - *pro*: SIMPLE, REASONABLE, LATERAL EFFECTS FREE - *cons*: JSON file remain for this key as "non-intuitive" information
        * 2. re-engineer `rdinv.py` to generate right info structure for this key - *pro*: right and intuitive JSON information presentation - *cons*: a lot of lateral effects, there is "a lot of code" that already extract only item 0 and this code could be in functions out of `rdinv.py` module, for example in `libutils.py`
        * 3. update module `rdinv.py` to preserve only index 0 **when create key `cac_InvoiceLine`, line ~408 so:**
            - ACTUAL value: `"cac_InvoiceLine": copy.deepcopy(tmp_InvoiceLine_list),`
            - DESIRED value:
                ```python
                "cac_InvoiceLine": copy.deepcopy(tmp_InvoiceLine_list)[0],
                ```
* `240306piu04` archived 0.3.0b & 0.3.1b versions





