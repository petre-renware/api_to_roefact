
rem copyright (c) 2024 Petre Iordanescu, petre.iordanescu@yahoo.com, RENware Software Systems
rem this command script will be run on CI automation workflow: >NUL
rem     - op sys: Windows >NUL
rem     - trigger event: merge to branch `adhoc` >NUL
rem     - stdout redirection: `./tests/_test_results.txt` >NUL



cd xl2roefact
python -m pip install pdm >NUL
python -m pdm install >NUL

rem pdm run build_doc

echo Show app version on SEXE run
.\dist\xl2roefact-0.5.4-win64.exe -V


