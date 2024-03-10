
rem ---------------
rem copyright (c) 2024 Petre Iordanescu, petre.iordanescu@yahoo.com, RENware Software Systems
rem this command script will be run on CI automation workflow;
rem     - workflow; `adhoc-run.yml`
rem     - trigger event: merge to branch `adhoc`
rem     - stdout redirection: `./tests/_test_results.txt`
rem     - crt directory; `xl2roefact/`
rem -------------------------

rem echo "=== Test run of `adhoc.cmd` ======"



rem wip.tests.... pdm run pypi_publish >_test_results.txt

rem ...wip.tests ... pyinstaller 
mklink xl2roefact.py xl2roefact_symlink_for_sexe.py
rem pdm run build_sexe



