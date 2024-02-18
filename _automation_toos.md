
# Automation tools

## Build site

Merge branch which contains `mkdocs` site to build into branch **`build-site`**.
The site will be built according to `mkdocs.yml` specs.


## Build xl2roefact CLI app, library packages and DLD doc

Merge to branch **`build-xl2roefact`**. The building process will execute `pdm run build_all` command in directory `xl2roefact/`.
Get back results by merging `build-xl2roefact` branch back to your initial branch.


## Run xl2roefact CLI app

Commit to branch **`...`**. The process will execute `pdm run xl2roefact xl2json -d ./tests >./tests/_test_on_git_results.txt` in directory `xl2roefact/`.
Results of execution are written on `xl2roefact/tests/` and `stdout` redirected to file `_test_on_git_results.txt`.



