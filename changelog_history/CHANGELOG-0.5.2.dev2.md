**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.5.2.dev2


### `0.5.2.dev2` release xl2roefact.`0.4.1.dev1` fix sEXE bug from `0.4.1.dev0` version:

* [x] 1. update `config_settings.py` module to load app cfg from external file only when not sEXE frozen app (`getattr(sys, 'frozen', False) == True`)
* [x] 2. update xl2roefact version to `0.4.1.dev1` to generate only sEXE deliverable
* [x] 3. test python code. Result: **PASS**
* [x] 4. generate sEXE
* [x] 5. test `pdm run xl2roefact settings`. Result: **PASS**
* [x] 6. clean and make code "production like"
* [x] 7. update INVOICEtoROefact project `versions.yml`:
    * xl2roefact = 0.4.1.dev1
    * INVOICEtoROefact = 0.5.2.dev2
* [x] 8. build xl2roefact wheel and DLD doc
* [x] 9. publish `0.4.1.dev1` on PyPi
* [x] 10. build all deliverables
* [x] 11. update downloads.md ref all deliverables
* build site & publish





