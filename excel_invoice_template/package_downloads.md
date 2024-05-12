
<small>**RENware Software Systems**</small>

<!--NOTE: DISCLAIMER -->

!!! warning "Versiuni END OF LIFE"
    Versiunile `<= 0.5` nu vor mai fi intretinute si nici disponibile incepind de la 01-May-2024 (*end of life*).

!!! warning "Versiunile development"
    Versiunile ce contin in codul / numarul lor acronimul `dev` sunt considerate versiuni elaborate in faza de dezvoltare software.
    Aceste versiuni sunt functionale dar testate doar cu date de test si nu cu date de business.
    Se recomanda a folosi aceste versiuni doar pentru dezvoltari proprii sau integrari cu alte sisteme.




# xl2roefact - resurse pentru descarcare (downloads)

<!--NOTE: intentionally start with Heading-1 and no TOC in this doc -->


## Format sursa biblioteca Python  <a id="format-biblioteca-python"></a>


### xl2roefact pe PyPi  <a id="pachetul-xl2roefact-pe-pypi"></a>
Versiunea de pe pe repository-ul public `PyPi` permite instalarea directa in mediul Python local astfel:
```shell
pip install xl2roefact
```
In acest mod va fi instalata automat ultima versiune stabila publicata pe *[PyPi](https://pypi.org/project/xl2roefact/)*. Accesati linkul anterior pentru a putea accesa alte versiuni publicate pe *PyPi* si modul de instalare a acestora.


### xl2roefact pachete redistribuibile   <a id="pachetul-xl2roefact-python-library-format-sursa"></a>
<!--NOTE: starting with `0.6rc0` source deliverables are available only on `PyPi` -->

??? note "0.7"
    * [`0.7rc2` updated console application to run in  silent or vebosed](https://pypi.org/project/xl2roefact/0.7rc2/)
    * [`0.7rc1` review & clean `xl2roefact.rdinv` module of TODOs](https://pypi.org/project/xl2roefact/0.7rc1/)    
    * [`0.7rc0` settings refresh option and app settings reload by request](https://pypi.org/project/xl2roefact/0.7rc0/)

??? note "0.6"
    * [`0.6` invoice type JSON-XML tag](https://pypi.org/project/xl2roefact/0.6)
    * [`0.6rc0` system database and parameters](https://pypi.org/project/xl2roefact/0.6rc0/)

<!-- #TODO; from 240501 drop these versions as deprecated -->
<!--NOTE: for each version there is a pair: WHEEL & DIST -->

??? note "0.5"
    * [`0.5.4` invoice supplier from owner master data WHEEL](../xl2roefact/dist/xl2roefact-0.5.4-py3-none-any.whl "download")
    * [`0.5.4` invoice supplier from owner master data DIST](../xl2roefact/dist/xl2roefact-0.5.4.tar.gz "download")
    * [`0.5.3rc1` fix invoice JSON key "cac:Party" naming WHEEL](../xl2roefact/dist/xl2roefact-0.5.3rc1-py3-none-any.whl "download")
    * [`0.5.3rc1` fix invoice JSON key "cac:Party" naming DIST](../xl2roefact/dist/xl2roefact-0.5.3rc1.tar.gz "download")
    * [`0.5.3rc0` invoice supplier from Excel WHEEL](../xl2roefact/dist/xl2roefact-0.5.3rc0-py3-none-any.whl "download")
    * [`0.5.3rc0` invoice supplier from Excel DIST](../xl2roefact/dist/xl2roefact-0.5.3rc0.tar.gz "download")

??? note "0.4"
    * [`0.4.1.dev1` fix sEXE bug from v(0.4.1.dev0) version WHEEL](../xl2roefact/dist/xl2roefact-0.4.1.dev1-py3-none-any.whl "download")
    * [`0.4.1.dev1` fix sEXE bug from v(0.4.1.dev0) version DIST](../xl2roefact/dist/xl2roefact-0.4.1.dev1.tar.gz "download")
    * [`0.4.1.dev0` xl2roefact include a data directory in package WHEEL](../xl2roefact/dist/xl2roefact-0.4.1.dev0-py3-none-any.whl "download")
    * [`0.4.1.dev0` xl2roefact include a data directory in package DIST](../xl2roefact/dist/xl2roefact-0.4.1.dev0.tar.gz "download")
    * [`0.4.0.dev2` externalize recommended rules for updating app setting rules WHEEL](../xl2roefact/dist/xl2roefact-0.4.0.dev2-py3-none-any.whl "download")
    * [`0.4.0.dev2` externalize recommended rules for updating app setting rules DIST](../xl2roefact/dist/xl2roefact-0.4.0.dev2.tar.gz "download")
    * [`0.4.0.dev1` fixed `xl2roefact` CLI app version addressing WHEEL](../xl2roefact/dist/xl2roefact-0.4.0.dev1-py3-none-any.whl "download")
    * [`0.4.0.dev1` fixed `xl2roefact` CLI app version addressing DIST](../xl2roefact/dist/xl2roefact-0.4.0.dev1.tar.gz "download")

??? note "0.3"
    * [`0.3.1b1` fixed bug JSON->["Invoice"]["cac_InvoiceLine"] list[list] WHEEL](../xl2roefact/dist/xl2roefact-0.3.1b1-py3-none-any.whl "download")
    * [`0.3.1b1` fixed bug JSON->["Invoice"]["cac_InvoiceLine"] list[list] DIST](../xl2roefact/dist/xl2roefact-0.3.1b1.tar.gz "download")
    * [`0.3.1b` xl2roefact documentation fixes WHEEL](../xl2roefact/dist/xl2roefact-0.3.1b0-py3-none-any.whl "download")
    * [`0.3.1b` xl2roefact documentation fixes DIST](../xl2roefact/dist/xl2roefact-0.3.1b0.tar.gz "download")
    * [`0.3.0b` xl2roefact invoice taxes summary WHEEL](../xl2roefact/dist/xl2roefact-0.3.0b0-py3-none-any.whl "download")
    * [`0.3.0b` xl2roefact invoice taxes summary DIST](../xl2roefact/dist/xl2roefact-0.3.0b0.tar.gz "download")

??? note "0.2"
    * [`0.2.1b` invoice values summary WHEEL](../xl2roefact/dist/xl2roefact-0.2.1b0-py3-none-any.whl "download")
    * [`0.2.1b` invoice values summary DIST](../xl2roefact/dist/xl2roefact-0.2.1b0.tar.gz "download")
    * [`0.2.0b` invoice customer info-optional items (bank, email, reg-com, phone) WHEEL](../xl2roefact/dist/xl2roefact-0.2.0b0-py3-none-any.whl "download")
    * [`0.2.0b` invoice customer info-optional items (bank, email, reg-com, phone) DIST](../xl2roefact/dist/xl2roefact-0.2.0b0.tar.gz "download")

??? note "0.1"
    * [`0.1.22b` application interface improvements WHEEL](../xl2roefact/dist/xl2roefact-0.1.22b0-py3-none-any.whl "download")
    * [`0.1.22b` application interface improvements DIST](../xl2roefact/dist/xl2roefact-0.1.22b0.tar.gz "download")
    * [`0.1.20.dev` invoice customer address WHEEL](../xl2roefact/dist/xl2roefact-0.1.20-py3-none-any.whl "download")
    * [`0.1.20.dev` invoice customer address DIST](../xl2roefact/dist/xl2roefact-0.1.20.tar.gz "download")






## Windows x64   <a id="format-executabil-windows-x64"></a>

### xl2roefact linie comanda kit instalare (win64-msi)   <a id="aplicatia-xl2roefact-linie-comanda-pachet-instalare-win64-msi"></a>

??? note "0.7"
    * [`0.7rc2` updated console application to run in  silent or vebosed](../xl2roefact/dist/xl2roefact-0.7rc2-win64.msi "download")
    * `0.7rc1` review & clean `xl2roefact.rdinv` module of TODOs - INDISPONIBILA
    * [`0.7rc0` settings refresh option and app settings reload by request](../xl2roefact/dist/xl2roefact-0.7rc0-win64.msi "download")

??? note "0.6"
    *  [`0.6` invoice type JSON-XML tag](../xl2roefact/dist/xl2roefact-0.6-win64.msi "download")
    * `0.6rc0 system database and parameters` - INDISPONIBILA

<!-- #TODO; from 240501 drop these versions as deprecated -->

??? note "0.5"
    * [`0.5.4` invoice supplier from owner master data](../xl2roefact/dist/xl2roefact-0.5.4-win64.msi "download")
    * [`0.5.3rc1` fix invoice JSON key "cac:Party" naming](../xl2roefact/dist/xl2roefact-0.5.3rc1-win64.msi "download")
    * [`0.5.3rc0` invoice supplier from Excel](../xl2roefact/dist/xl2roefact-0.5.3rc0-win64.msi "download")

??? note "0.4"
    * [`0.4.1.dev1` fix sEXE bug from v(0.4.1.dev0) version](../xl2roefact/dist/xl2roefact-0.4.1.dev1-win64.msi "download")
    * [`0.4.1.dev0` xl2roefact include a data directory in package](../xl2roefact/dist/xl2roefact-0.4.1.dev0-win64.msi "download")
    * [`0.4.0.dev2` externalize recommended rules for updating app setting rules](../xl2roefact/dist/xl2roefact-0.4.0.dev2-win64.msi "download")

??? note "0.3"
    * [`0.3.1b1` fixed bug JSON->["Invoice"]["cac_InvoiceLine"] list[list]](../xl2roefact/dist/xl2roefact-0.3.1b1-win64.msi "download")
    * [`0.3.1b` xl2roefact documentation fixes](../xl2roefact/dist/xl2roefact-0.3.1b0-win64.msi "download")
    * [`0.3.0b` xl2roefact invoice taxes summary](../xl2roefact/dist/xl2roefact-0.3.0b0-win64.msi "download")

??? note "0.2"
    * [`0.2.1b` xl2roefact invoice values summary](../xl2roefact/dist/xl2roefact-0.2.1b0-win64.msi "download")
    * [`0.2.0b` invoice customer info-optional items (bank, email, reg-com, phone)](../xl2roefact/dist/xl2roefact-0.2.0b0-win64.msi "download")

??? note "0.1"
    * [`0.1.22b` application interface improvements](../xl2roefact/dist/xl2roefact-0.1.22b0-win64.msi "download")
    * [`0.1.20.dev` invoice customer address](../xl2roefact/dist/xl2roefact-0.1.20-win64.msi "download")


### xl2roefact linie comanda executabil portabil (win64-exe)   <a id="aplicatia-xl2roefact-linie-comanda-executabil-portabil-win64-exe"></a>

??? note "0.7"
    * [`0.7rc2` updated console application to run in  silent or vebosed](../xl2roefact/dist/xl2roefact-0.7rc2-win64.exe "download")
    * `0.7rc1` review & clean `xl2roefact.rdinv` module of TODOs - INDISPONIBILA
    * [`0.7rc0` settings refresh option and app settings reload by request](../xl2roefact/dist/xl2roefact-0.7rc0-win64.exe "download")

??? note "0.6"
    *  [`0.6` invoice type JSON-XML tag](../xl2roefact/dist/xl2roefact-0.6-win64.exe "download")
    * `0.6rc0 system database and parameters` INDISPONIBILA

<!-- #TODO; from 240501 drop these versions as deprecated -->

??? note "0.5"
    * [`0.5.4` invoice supplier from owner master data](../xl2roefact/dist/xl2roefact-0.5.4-win64.exe "download")
    * [`0.5.3rc1` fix invoice JSON key "cac:Party" naming](../xl2roefact/dist/xl2roefact-0.5.3rc1-win64.exe "download")
    * [`0.5.3rc0` invoice supplier from Excel](../xl2roefact/dist/xl2roefact-0.5.3rc0-win64.exe "download")

??? note "0.4"
    * [`0.4.1.dev1` fix sEXE bug from v(0.4.1.dev0) version](../xl2roefact/dist/xl2roefact-0.4.1.dev1-win64.exe "download")
    * ***known bug DO NOT USE*** [`0.4.1.dev0` xl2roefact include a data directory in package](../xl2roefact/dist/xl2roefact-0.4.1.dev0-win64.exe "download")
    * [`0.4.0.dev2` externalize recommended rules for updating app setting rules](../xl2roefact/dist/xl2roefact-0.4.0.dev2-win64.exe "download")

??? note "0.3"
    * [`0.3.1b1` fixed bug JSON->["Invoice"]["cac_InvoiceLine"] list[list]](../xl2roefact/dist/xl2roefact-0.3.1b1-win64.exe "download")


### web2roefact kit instalare (win64-msi)   <a id="aplicatia-web2roefact-pachet-instalare-win64-msi"></a>
Nici o resursa disponibila.





## Linux   <a id="format-deb-instalare-linux"></a>
Nici o resursa disponibila.


## MacOS X  <a id="format-instalare-macosx"></a>
Nici o resursa disponibila.






## Sablon template factura   <a id="sablon-template-factura"></a>

??? note "Format XLSX Office Excel"
    * [`0.1.20` office Excel XLSX](../excel_invoice_template/invoice_template_CU_tva.xlsx "download")
    * [`0.1.20` arhiva ZIP](../excel_invoice_template/released_packages/0.1.20-excel_invoice_template.zip "download")
    * [`0.1.11` arhiva ZIP](../excel_invoice_template/released_packages/0.1.11-excel_invoice_template.zip "download")






## Sablon fisier configurare a aplicatiei xl2roefact   <a id="sablon-fisier-configurare-a-aplicatiei-xl2roefact"></a>
Sablonul permite configurarea aplicatiei prin modificarea fragmentelor de text care trebuiesc cautate in fisierul Excel pentru identificarea diverselor informatii aferente facturii.

Sablonul este in format [YAML](https://yaml.org/) iar informatiile ce trebuiesc descrise sunt explicate individual in comentarii insotitoare.
De asemenea este util a fi citite si recomandarile date in pagina de descriere a aplicatiei.

Pentru a beneficia de cobfigurarile facute de dumneavoastra trebuie sa creati un fisier **`app_settings.yml`** in directorul curent din care lansati aplicatia, fisier ce contine noile configurari dorite.
**Numele fisierelui este obligatoriu a fi respectat.**

!!! info "Fisiere de configurare multiple"
    De retinut ca acest fisier este considerat (daca exista) cel din directorul curent de unde lansati aplicatia. Deci daca v-ati creat mai multe directoare de lucru (de exemplu pentru clienti diferiti) puteti crea fisiere de configurare specifice, cite unul in fiecare director.

* [Descarcare sablon de fisier de configurare](./../xl2roefact/xl2roefact/data/app_settings.yml "download")

!!! tip "Continutul sablonolui"
    De mentionat ca acest sablon este pre-completat cu situatii curent intilnite in practica, el fiind chiar sablonul implicit folosit de aplicatie.






+++ 0.6

## Sablon fisier cu date furnizor  <a id="sablon-fisier-cu-date-furnizor"></a>

* [Descarcare fisier cu date furnizor](./../xl2roefact/doc/owner_datafile_tmeplate.yml "download")



