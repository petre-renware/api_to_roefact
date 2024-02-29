**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.2.1b


### 0.2.1b xl2roefact invoice values summary (240225 h18:30)

* `240221piu_a` invoice grand totals
    * [x] 1. new function `dict_sum_by_key(...)` to sum a dict at all levels for a key. Implemented in `xl2roefact libutils` module.
    * [x] 2. doc with wk.specs ref summary structure `.../xl2roefact/tests/_tmp_wkdoc_invoice_summary.md` (NOTE: will be deleted after finish)
    * [x] 3. created work JSON-XML map required structure in `.../xl2roefact/tests/__invoice_summary.md`
    * [x] 4. code for some calculations, test & fix formulas
    * [x] 5. update JSON-XML map in code (rdinv.py)
* `200220piu_b` init a PDM simple env in project root
    * [x] 1. root project is for SITE GENERATION
    * [x]  2. project name set to **INVOICEtoROefact** and the version dynamic from `/__version__.py`
    * [x] 3. updated `pyproject.toml` default dependencies
    * [x] 4. incomplete finalized PDM usage. Run `pdm init` then `pdm update` to get dependencies
      _RESOLUTION:_ item 4. will be finalied in next releases because is a long run task under Windows
* `240220piu_a` reorganized `INVOICEtoROeFact` project by preparing python directory structure for **`web2roefact`** component as installable package (model xl2roefact)





