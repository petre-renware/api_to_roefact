**api-to-roefact by RENware Software Systems**

[TOC]


# CHANGELOG 0.5.4


## `0.5.4` invoice supplier from owner master data (240406 h22:00)

* `upd-dwnld-0.5.4` update `downloads.md` for 0.5.4 deliverables
* `build-apps-0.5.4` build all deliverables & publish package on PyPi
* `prep-rlse-0.5.4` change this head to `0.5.4` version, update all `/versions.yml` and assure that all are published
* `fix-download-owner-template` xl2roefact README sectiune "Descarcare (download) aplicatie xl2roefact CLI" de pus link catre sablon nomenclator furnizori
* `fixed-tech-doc` generatorul plugin mkdocs ptr comenzile Typer nu a generat complet... A ramas ca inainte de modificare 0.5.4... adica nu apare optiunea `-o  -owner-file`
* * `owner-dbs-file` get OWNER EXTERNAL DATA feature (version `0.5.4.dev0+owner-dbs-file`):
    * [x] 1. create `data/owner.yml` structure to exactly what is needed for actual JSON "Invoice..." key
    * [x] 2. created a skeleton for `hier_get_data_file()` module, update its docstring and generate DLD documentation
    * [x] 3. set a new flag for `xl2json` command for getting owner from ext data-file: `--owner -o [FILE]` where `FILE` being defaulted to `./owner.yml` or hierarchy to `data/owner.yml`
    * [x] 4. app_cli.py chk if file is ok and sent it as correct Path if, else raise an err msg and continue from Excel
    * [x] 5. code. Get owner data by using function `hier_get_data_file()`
    * [x] 6. update `owner.yml` file and add bank information
    * [x] 7. code. Get owner bank information from external data file
    * [x] 8. build xl2roefact DLD documentation
    * [x] 9. code. Review "place where called for OWNER info", clean, update and close code
    * [x] 10. make template for owner data file (`owner_datafile_tmeplate.yml`) and prep it with built-in documentation hints
    * [x] 11. updated temporary all version to `0.5.4.dev0` to make DEV publishes (basically for site, but other tests are possibile)
    * [x] 12. add xl2roefact README doc with section "Utilizare nomenclator de furnizori"
    * [x] 13. build site and publish as site version `0.5.4.dev0` (temporary value)
* `hier-get-data-file` func to select hierarchical a file from `./` or `data/` (in libutils module):
    * [x] 1. create skeleton `hier_get_data_file(file_name: str) -> Path` in `xl2roefact.libutils` module
    * [x] 2. code function to solve actual functional case from `xl2roefact.config_settings` module
    * [x] 3. update `xl2roefact.config_settings` module to use the new function


