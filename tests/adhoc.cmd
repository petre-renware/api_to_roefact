
rem copyright (c) 2024 Petre Iordanescu, petre.iordanescu@yahoo.com, RENware Software Systems
rem this command script will be run on CI automation workflow: >NUL
rem     - op sys: Windows >NUL
rem     - trigger event: merge to branch `adhoc` >NUL
rem     - stdout redirection: `./tests/_test_results.txt` >NUL




cd xl2roefact
python -m pip install pdm >NUL
python -m pdm install >NUL

echo Request help
pdm run xl2roefact xl2json --help

echo Run NORMAL
pdm run xl2roefact xl2json

echo Run WITH OWNER dataFILE
pdm run xl2roefact xl2json --owner-datafile file-owner.crt.dir


rem cd tests
rem .\xl2roefact-0.4.1.dev1-win64.exe settings -r


