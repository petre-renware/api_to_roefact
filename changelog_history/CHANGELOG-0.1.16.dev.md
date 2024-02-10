**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.1.16.dev

### 0.1.16.dev improving Excel kv-data search with "IN-LABEL" method (231222 h07:00)

* 231222piu_b build packages for:
    * [x] application deployment package ==> `dist/0.1.13-xl2roefact-0.1-win64.msi`
    * [x] cleaned, tested, created packages (saved to ==> `.../880-RLSE/880.90-RLSE Source Code Archives`)
    * [x] updated `pyproject.toml`

* 231222piu_a refactor `rdinv.__get_excel_data_at_label(...)` to search in label (named "IN-LABEL" method)

* 231220piu_b made a first PDM build: [@ 231220 h09:55] ==> test PASS (both created files in `dist/` was "git-ignored")

* 231220piu_b refactored `rdinv(...)` section "section for search of `invoice_items_area` ..." to use `__get_excel_data_at_label(...)` function`

* 231220piu_a refactored `rdinv.__get_excel_data_at_label(...)` for returned "label_position" key`

* 231219piu_a update `rdinv.__get_excel_data_at_label(...)` to return found label value in dictionary as key `"label_value"`

* 231218piu_c `PDM` environment manager, updated `pyproject.toml` structures ref package building, still preps to create env, generate lock file...

* 231218piu_b CLI application, fixed bug of print settings when deployed from a package (command: `xl2roefact.py settings`)

* 231218piu_a installed `PDM` environment manager, updated `pyproject.toml` structures, nxt to create env, generate lock file...




