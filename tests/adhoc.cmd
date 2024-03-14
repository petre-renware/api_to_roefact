
rem ---------------
rem copyright (c) 2024 Petre Iordanescu, petre.iordanescu@yahoo.com, RENware Software Systems
rem this command script will be run on CI automation workflow:
rem     - op sys: Windows
rem     - workflow; `adhoc-run.yml`
rem     - trigger event: merge to branch `adhoc`
rem     - stdout redirection: `./tests/_test_results.txt`





rem *** Change directory to XL2ROEFACT project component
cd xl2roefact

rem Create needed environment
python -m pip install pdm
python -m pdm install

rem Effective script
pdm info



rem *** Change directory to INVOICETOROEFACT project component
cd ..

rem Create needed environment
python -m pip install pdm
python -m pdm install

rem Effective script
pdm info







rem *** to build standalone EXE
rem pdm run build_sexe


