**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.4.0.dev2


### 0.4.0.dev2 externalize recommended rules for updating app setting rules (240316 T12:00)

* `0.4.0.dev2` externalize recommended rules for updating app setting rules
    * [x] 1. created `xl2roefact/data/README_app_config_rules.md` containing the recommended rules for updating app setting rules
    * [x] 2. refer it in `config_settings.py` in its docstring section ==> exported `rules_content` that contain text
    * [x] 3. update `app_cli.py` module to load them accordingly on `settings --rules` command + option
    * [x] 4. build this package and publish on PyPi
    * archived locally (RLSE) package wheel & dist
    * [x] 5. update `xl2roefact README` to reflect that change
    * [x] 6. build all deliverables
    * [x] 7. update `downloads.md` with section for "Other resource downloads" with doc from item 1
* `240314piu01` update GitHub `ad hoc` workflow, made usable for any project component by moving structures to project root and letting environment management at command script glance
* `0.4.0.dev1` fixed `xl2roefact` CLI app version addressing
* `0.4.0.dev0` updated `xl2roefact.__init__.py` to expose public symbols
* `240313piu02` small administrative adjustments: update technical axl2roefact DLD, build site & republish (used version `0.4.0rc0` for whole system)
* `240313piu01` application tech optimizations: `rdinv.__all__` spec, `__init__.__version__` import and made available as xl2roefact global












