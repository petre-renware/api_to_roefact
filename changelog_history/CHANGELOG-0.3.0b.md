**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.3.0b


### 0.3.0b xl2roefact invoice taxes summary (240306 07:00)

* `240302piu03` invoice taxes summary:
    * ref doc `xl2roefact/invoice_files/_PLAN_model...xml`, lines 91-104)
    * prepared place in rdinv() search "NOTE: ....place intended for `cac:TaxTotal`" line ~413
    * [x] 1. prepared a work file `xl2roefact/tests/__wk_invoice_tax_total.md` with dev specs & TODOs
    * [x] 2. defined calculation formulas in `xl2roefact/tests/__wk_invoice_tax_total.md`
    * [x] 3. made a function skeleton `invoice_taxes_summary(invoice_lines: list[dict])` in `libutils` that calculates whole required structure. Receive as parameter the `Invoice dict` part related to items list, ie existing variable `tmp_InvoiceLine_list`
    * [x] 4. calculated `cac_TaxTotal` calculation code of item 3. in function `libutils.invoice_taxes_summary(...)`. Code test PASS. Function closed
    * [x] 5. updated XML-JSON map
    * [x] 6. calculated cbc_TaxAmount
    * [x] 7. update JSON example used in documentation
    * [x] 8. updated version number of xl2roefact app (component & mkdocs.yml)
    * [x] 9. run `pdm build_all` ==> version deliverables incl DLD doc
    * [x] 10.a update `downloads.md` with `0.3.0b` deliverables
    * [x] 10.b build site & publish
    * [x] 10.c publish library on PyPi (use CI workflow by branch `pypi-publish`)
    * [x] 11. clean code, drop `xl2roefact/tests/__wk_invoice_tax_total.md
* `240301piu02` refactored `xl2roefact/invoice_files/` to `xl2roefact/refact_xml_models_and_specs/`
* `240302piu01` updated `xl2rofact.rdinv` function, area commented "...build final structure..." created variable `_tmp_reusable_items: dict` to keep "partial variables" that are calculated and potentially will be reused in next code
* `240301piu_01` set all workflows `run-name`


