
<small>**RENware Software Systems**</small>

<!--NOTE: DISCLAIMER -->

!!! warning "Versiuni END OF LIFE"
    Versiunile `<= 0.5` nu vor mai fi intretinute si nici disponibile incepind de la 01-May-2024 (*end of life*).

!!! warning "Versiunile development"
    Versiunile ce contin in codul / numarul lor acronimul `dev` sunt considerate versiuni elaborate in faza de dezvoltare software.
    Aceste versiuni sunt functionale dar testate doar cu date de test si nu cu date de business.
    Se recomanda a folosi aceste versiuni doar pentru dezvoltari proprii sau integrari cu alte sisteme.


# Descarcare resurse (resources download)

[TOC]


## xl2roefact

### editia consola
...
### editia developer
...
### editia desktop
...
### editia mobila
...




## web2roefact
Indisponibila in aceasta versiune.





## Sablon template factura   <a id="sablon-template-factura"></a>
...





## Sablon fisier configurare a aplicatiei xl2roefact   <a id="sablon-fisier-configurare-a-aplicatiei-xl2roefact"></a>
Sablonul permite configurarea aplicatiei prin modificarea fragmentelor de text care trebuiesc cautate in fisierul Excel pentru identificarea diverselor informatii aferente facturii.

Sablonul este in format [YAML](https://yaml.org/) iar informatiile ce trebuiesc descrise sunt explicate individual in comentarii insotitoare.
De asemenea este util a fi citite si recomandarile date in pagina de descriere a aplicatiei.

Pentru a beneficia de cobfigurarile facute de dumneavoastra trebuie sa creati un fisier **`app_settings.yml`** in directorul curent din care lansati aplicatia, fisier ce contine noile configurari dorite.
**Numele fisierelui este obligatoriu a fi respectat.**

!!! info "Fisiere de configurare multiple"
    De retinut ca acest fisier este considerat (daca exista) cel din directorul curent de unde lansati aplicatia. Deci daca v-ati creat mai multe directoare de lucru (de exemplu pentru clienti diferiti) puteti crea fisiere de configurare specifice, cite unul in fiecare director.

* [Descarcare fisier sablon de configurare](./../xl2roefact/xl2roefact/data/app_settings.yml "download")

!!! tip "Continutul sablonului"
    De mentionat ca acest sablon este pre-completat cu situatii curent intilnite in practica, el fiind chiar sablonul implicit folosit de aplicatie.




## Sablon fisier cu date furnizor  <a id="sablon-fisier-cu-date-furnizor"></a>

* [Descarcare fisier sablon date furnizor](./../xl2roefact/doc/owner_datafile_tmeplate.yml "download") 





