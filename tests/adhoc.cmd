
rem copyright (c) 2024 Petre Iordanescu, petre.iordanescu@yahoo.com, RENware Software Systems
rem this command script will be run on CI automation workflow:
rem     - op sys: Windows
rem     - trigger event: merge to branch `adhoc`
rem     - stdout redirection: `./tests/_test_results.txt`




cd xl2roefact

python -m pip install pdm
python -m pdm install

pdm run xl2roefact --version

pdm run xl2roefact settings








rem *** to build standalone EXE
rem pdm run build_sexe


