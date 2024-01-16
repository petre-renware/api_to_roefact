**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.1.11.dev


* 231209piu_c build packages for:
    * [x] application deployment package ==> `dist/0.1.11-xl2roefact-0.1-win64.msi`
    * [x] excel invoice template package ==> `dist/0.1.11-excel_invoice_template.zip`
    * [x] cleaned, tested, created packages (saved to ==> `.../880-RLSE/880.90-RLSE Source Code Archives`)

* 231209piu_b **fixed `xl2roefact` CLI options, help, defaults, short names** and __STABILIZED EXECUTION__

* closed `231209piu_a` more actions:
    * changed `README.md`: translated to RO, updated installation & usage information
    * dropped old, obsolete deployment packages
    * test PASS

* 231208piu_b add an INVOICE TEMPLATE (`excel_invoice_template/invoice_template_CU_tva.xlsx`) as deliverable with application

* 231208piu_a review, cleaning and formatting code (generalized & moved some debug-verbose code from `rdinv` to `xl2roefact.xl2json`), test PASS
* 231207piu_b cleaned `rdinv` of "...for debug purposes..." prints, test PASS

* 231207piu_c reviewed and updated `xl2roefact`: README, LICENSE, pyproject.toml
