
<small>**RENware Software Systems**</small>


# xl2roefact - resurse pentru descarcare (downloads)

[TOC]




## Formate sursa biblioteca Python
<a id="format-biblioteca-python"></a>


### xl2roefact din PyPi
<a id="pachetul-xl2roefact-pe-pypi"></a>
Versiunea de pe pe repository-ul public `PyPi` permite instalarea directa in mediul Python local astfel:
```shell
pip install xl2roefact
```
In acest mod va fi instalata automat *ultima versiune stabila* publicata pe *[PyPi](https://pypi.org/project/xl2roefact/)*. Accesati linkul anterior pentru a putea accesa alte versiuni publicate pe *PyPi* si modul de instalare a acestora.


### xl2roefact pachete sursa versiuni anterioare
<a id="pachetul-xl2roefact-python-library-format-sursa"></a>

??? note "0.8"
    * [`0.8` BUGFIX xl2roefact entry point](https://pypi.org/project/xl2roefact/0.8/)

??? note "0.7"
    * [`0.7` clean xl2roefact package and invoice JSON](https://pypi.org/project/xl2roefact/0.7/)
    * [`0.7rc2` updated console application to run in  silent or vebosed](https://pypi.org/project/xl2roefact/0.7rc2/)
    * [`0.7rc1` review & clean `xl2roefact.rdinv` module of TODOs](https://pypi.org/project/xl2roefact/0.7rc1/)    
    * [`0.7rc0` settings refresh option and app settings reload by request](https://pypi.org/project/xl2roefact/0.7rc0/)

??? note "0.6"
    * [`0.6` invoice type JSON-XML tag](https://pypi.org/project/xl2roefact/0.6)
    * [`0.6rc0` system database and parameters](https://pypi.org/project/xl2roefact/0.6rc0/)






## Formate pentru Windows x64
<a id="format-executabil-windows-x64"></a>

### xl2roefact linie comanda kit instalare (win64-msi)
<a id="aplicatia-xl2roefact-linie-comanda-pachet-instalare-win64-msi"></a>

??? note "0.8"
    * `0.8` BUGFIX xl2roefact entry point - INDISPONIBILA

??? note "0.7"
    * [`0.7` clean xl2roefact package and invoice JSON](../dist/xl2roefact-0.7-win64.msi "download")
    * [`0.7rc2` updated console application to run in  silent or vebosed](../dist/xl2roefact-0.7rc2-win64.msi "download")
    * `0.7rc1` review & clean `xl2roefact.rdinv` module of TODOs - INDISPONIBILA
    * [`0.7rc0` settings refresh option and app settings reload by request](../dist/xl2roefact-0.7rc0-win64.msi "download")

??? note "0.6"
    *  [`0.6` invoice type JSON-XML tag](../dist/xl2roefact-0.6-win64.msi "download")
    * `0.6rc0 system database and parameters` - INDISPONIBILA




### xl2roefact linie comanda executabil portabil (win64-exe)
<a id="aplicatia-xl2roefact-linie-comanda-executabil-portabil-win64-exe"></a>

??? note "0.8"
    * `0.8` BUGFIX xl2roefact entry point - INDISPONIBILA

??? note "0.7"
    * [`0.7` clean xl2roefact package and invoice JSON](../dist/xl2roefact-0.7-win64.exe "download")
    * [`0.7rc2` updated console application to run in  silent or vebosed](../dist/xl2roefact-0.7rc2-win64.exe "download")
    * `0.7rc1` review & clean `xl2roefact.rdinv` module of TODOs - INDISPONIBILA
    * [`0.7rc0` settings refresh option and app settings reload by request](../dist/xl2roefact-0.7rc0-win64.exe "download")

??? note "0.6"
    *  [`0.6` invoice type JSON-XML tag](../dist/xl2roefact-0.6-win64.exe "download")
    * `0.6rc0 system database and parameters` INDISPONIBILA





## Sablon fisier configurare a aplicatiei xl2roefact
<a id="sablon-fisier-configurare-a-aplicatiei-xl2roefact"></a>

Sablonul permite configurarea aplicatiei prin modificarea fragmentelor de text care trebuiesc cautate in fisierul Excel pentru identificarea diverselor informatii aferente facturii.

Sablonul este in format [YAML](https://yaml.org/) iar informatiile ce trebuiesc descrise sunt explicate individual in comentarii insotitoare.
De asemenea este util a fi citite si recomandarile date in pagina de descriere a aplicatiei.

Pentru a beneficia de cobfigurarile facute de dumneavoastra trebuie sa creati un fisier **`app_settings.yml`** in directorul curent din care lansati aplicatia, fisier ce contine noile configurari dorite.
**Numele fisierelui este obligatoriu a fi respectat.**

!!! info "Fisiere de configurare multiple"
    De retinut ca acest fisier este considerat (daca exista) cel din directorul curent de unde lansati aplicatia. Deci daca v-ati creat mai multe directoare de lucru (de exemplu pentru clienti diferiti) puteti crea fisiere de configurare specifice, cite unul in fiecare director.

* [Descarcare sablon de fisier de configurare](./../xl2roefact/data/app_settings.yml "download")

!!! tip "Continutul sablonolui"
    De mentionat ca acest sablon este pre-completat cu situatii curent intilnite in practica, el fiind chiar sablonul implicit folosit de aplicatie.







## Sablon fisier cu date furnizor
<a id="sablon-fisier-cu-date-furnizor"></a>

* [Descarcare fisier cu date furnizor](./../doc/owner_datafile_tmeplate.yml "download")




