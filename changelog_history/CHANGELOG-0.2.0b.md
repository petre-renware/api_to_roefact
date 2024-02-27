**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.2.0b


### `0.2.0b` xl2roefact invoice customer info - optional items (bank, email, reg-com, phone) (240220 h10:00)

* 240219piu_a invoice customer search for other keys: "reg com", "bank / IBAN / cont", "phone", "email"
    * [x] 1. read req information and stored in local vars, as full dict (for excel original key) and as cleaned (for invoice key)
    * [x] 2. store info in `customer_header_area` --> `excel...original` data key
    * [x] 3.a. make a work-file with map XML-JSON ref key names (search in xml file for supplier area which is more elaborated)
    * [x] 3.b. update `customer_header_area` XML-JSON map key
    * [x] 3.c. store info in `customer_header_area` --> `Invoice` key
    * [x] 4. test app and its results. Clean up code
    * [x] 5.a. update tech doc ref JSON structure
    * [x] 5.b. build xl2roefact `0.2.0b`
    * [x] 6. update site documentation ref new xl2roefact deliverables download
    * [x] 7. build & publish, test site
* 240218piu_b created an automation workflow to run `xl2roefact xl2json` in directory `xl2roefact/tests/` and to obtain JSON of invoice to test it
    * [x] 1. moved test Excel invoices from `.../xl2roefact/invoice_files/` to `.../xl2roefact/tests/`
    * [x] 2. created automation YAML file (`run_xl2roefact.yml`)
    * [x] 3. test ==> PASS (exec results + `stdout --> _test_results.txt` written on `xl2roefact/tests/`)
* 240218piu_a documentation improvements by using dropdown items



