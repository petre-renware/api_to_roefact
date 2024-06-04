
# Automation tools

## Build site

Merge branch which contains `mkdocs` site to build into branch **`build-site`**.
The site will be built according to `mkdocs.yml` specs.



## Build xl2roefact CLI app, library packages, standalone EXE and DLD doc

Merge to branch **`build-xl2roefact`**. The building process will execute `pdm run build_all` command in directory `xl2roefact/`.
Get back results by merging `build-xl2roefact` branch back to your initial branch.



## PyPi publish of xl2roefact

Merge to branch **`pypi-publish`**. This workflow will initiate publishing to PyPi of the current built `xl2roefact` deliverables, WHEEL and DIST.



## Run xl2roefact CLI app

Commit to branch **`test-xl2roefact`**. The process will execute
```bash
pdm run xl2roefact xl2json -d ./tests >./tests/_test_on_git_results.txt
```
in directory `xl2roefact/`.
Results of execution are written on `xl2roefact/tests/` and `stdout` redirected to file `_test_on_git_results.txt`.



## Run adhoc commands in xl2roefact environment

Commit to branch **`adhoc`** and this automation CI will run any user defined command by **running Windows script `.../xl2roefact/tests/adhoc.cmd`**. Execution context:

- workflow; `adhoc-run.yml`
- trigger event: merge to branch `adhoc`
- stdout redirection: `./tests/_test_results.txt`
- crt directory; `xl2roefact/`




