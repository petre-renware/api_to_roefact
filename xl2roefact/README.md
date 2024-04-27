<small>**RENware Software Systems**</small>

# xl2roefact

![Static Badge](https://img.shields.io/badge/version-{{ xl2roefact_version }}-blue)

Legaturi externe utile:

* [**Web Site**](https://invoicetoroefact.renware.eu/). (*Pentru acces corect la toate referintele din acest document vizitati site-ul dedicat acestui sistem.*)
* [Pachet *PyPi*](https://pypi.org/project/xl2roefact/)
* [Surse *GitHub*](https://github.com/petre-renware/api_to_roefact/)
* [Referinta *dezvoltare software - biblioteca Python*](https://invoicetoroefact.renware.eu/xl2roefact/doc/README_xl2roefact_library.html)
* [Referinta *API*](https://invoicetoroefact.renware.eu/xl2roefact/doc/wrapper_810.05a-xl2roefact_DLD_specs.html)
<!--Refrence to source doc. If used like that, then must be resolved with an external tool before generating a complete README.html doc. The `mkdoxs` is able to do that but in `PyPi` published version will be unusable
(./doc/810.05a-xl2roefact_DLD_specs.md)
-->


## Facilitati

![Static Badge](https://img.shields.io/badge/MSI_installer-YES-darkgreen)
![Static Badge](https://img.shields.io/badge/standlone_EXE-YES-darkgreen)
![Static Badge](https://img.shields.io/badge/script_Python3-YES-darkgreen)
![Static Badge](https://img.shields.io/badge/pachet_DEB-in_curind-lightgrey)

![Static Badge](https://img.shields.io/badge/format_JSON-YES-orange)
![Static Badge](https://img.shields.io/badge/format_XML-YES-orange)
![Static Badge](https://img.shields.io/badge/format_PDF-YES-orange)
![Static Badge](https://img.shields.io/badge/format_RO_eFact-YES-red)



Aceasta componenta este "totul despre crearea de facturi electronice" din formatul Excel office (xlsx). Aplicatia poate genera factura in format JSON, XML, PDF si o poate incarca in sistemul *RO E-Fact*[^ld_roefact].

Aceasta componenta ofera urmatoarele facilitati (acestea fiind obiectivele fundamentale ale componentei):

* **transformarea facturilor din Excel in formatul `XML`** cerut de catre sistemul ANAF RO E-Fact pentru incarcare
* **incarcarea acestora** in sistemul ANAF RO E-Fact[^ld_roefact]
* **transformarea facturilor din Excel intr-un format `JSON`**  intermediar, independent de platforma si care permite integrarea acestora cu alte sisteme (standard *REST*)
* **generarea facturii in format PDF** pentru transmiterea acesteia catre client, semnarea electronica, tiparirea si arhivarea acesteia in format fizic (in general manipularea facturii in format *"human readable"*)

Componenta ofera doua instrumente pentru realizarea si indeplinirea acestor obiective:

* `xl2roefact` o **aplicatie de tip linie de comanda** (disponibila pentru sistemele de operare Windows, Linux si MacOS)
* `xl2roefact PyPi` **blioteca standard Python** utilizabila pentru dezvoltari proprii in scopul extinderii altor sisteme existente (*custom development*)






## Instalarea aplicatiei xl2roefact
Instalarea aplicatiei *xl2roefact* este disponibila in urmatoarele variante:

* pentru **Windows**:
    * **`MSI`** pachet instalare pentru *Windows*
    * **`EXE`** executabil *Windows in format "portabil" (un singur fisier)*

* pentru **Linux**:
    * _...in curind..._ **`DEB`** pachet instalare pentru *Linux Debian*  <!--#TODO: to.use `cxfreeze bdist_deb` -->
    * _...in curind..._ **`RPM`** pachet instalare pentru *Linux*  <!--#TODO: to.use `cxfreeze bdist_rpm` -->
    * _...in curind..._ **`APPIMG`** executabil *Linux in format "portabil" (un singur fisier)*  <!--#TODO: to.use `cxfreeze bdist_appimage` -->

* pentru **Mac OS X**
    * _...in curind..._ **`DMG`** pachet instalare pentru *MacOS*  <!--<!--#TODO: to.use `cxfreeze bdist_dmg` -->

* ca **script Python** indiferent de sistemul de operare;
    * **[Pachet Python](https://pypi.org/project/xl2roefact/)** biblioteca / libraria completa pe PyPi (inclusiv sursele)


>*Pentru acces la pachetele de instalare vezi [sectiunea de descarcare resurse](#descarcare-download-aplicatie-xl2roefact-cli).*

**Note:**
* *utilizarea ca script Python necesita existenta ca mediul *Python3 min 3.10* sa fie instalat local*
* numele pachetelor includ versiunea de aplicatie utilizata si sistemul de operare pentru care sunt disponibile
* pentru echivalent utilizare  *portabila pentru Linux* se poate instala biblioteca Python dupa care devine utilizabil scriptul Python "ca orice alta comanda Linux"






## Configurarea aplicatiei xl2roefact
Parametrii de configurare aplicatiei se gasesc in fisierul *`config_settings.py`*. Acestia sunt sub elaborati in limbaj Python prin utilizarea conventiilor de constante conform recomandarilor PEP (numele capitatlizat) si sunt acompaniti de linii de explicatii privind aplicabilitatea lor.

<!--#TODO: prev paragraph to replace new config method by using `app_settings.yml` in current directory -->

Configurare aplicatiei se poate face interactiv si din aplicatie. Pentru a obtine help referitor la detaliile comenzi se va folosi
```shell
xl2roefact settings --help
```

Configurarile existente si regulile recomandate in configurarea aplicatiei se afiseaza folosind comanda:
```shell
xl2roefact settings --rules
```


### Configurarea din fisier extern
Configurarea aplicatuiei se poate face si prin intermediul unui fisier extern numit "*sablon de configurare*" (*en: configuration template*). Sablonul permite configurarea aplicatiei prin modificarea fragmentelor de text care trebuiesc cautate in fisierul Excel pentru identificarea diverselor informatii aferente facturii.

Sablonul este in format [YAML](https://yaml.org/) iar informatiile ce trebuiesc descrise sunt explicate individual in comentarii insotitoare.
De asemenea este util a fi citite si recomandarile date in pagina de descriere a aplicatiei.

Pentru a beneficia de cobfigurarile facute de dumneavoastra trebuie sa creati un fisier **`app_settings.yml`** in directorul curent din care lansati aplicatia, fisier ce contine noile configurari dorite.
**Numele fisierelui este obligatoriu a fi respectat.**

!!! info "Fisiere de configurare multiple"
    De retinut ca acest fisier este considerat (daca exista) cel din directorul curent de unde lansati aplicatia. Deci daca v-ati creat mai multe directoare de lucru (de exemplu pentru clienti diferiti) puteti crea fisiere de configurare specifice, cite unul in fiecare director.


**Fisier de configurare global**

!!! info ""
    In conditiile folosirii kitului MSI pentru o instalare locala a aplicatiei (cu utilizari multiple si repetate) si in situatia in care se doreste schimbarea configurarii implicite a aplicatiei se vor urma acesti pasi:
    
    * in directorul de instalare a aplicatiei se va crea daca nu exita directorul `data/`
    * in acest director se va crea un fisier `app_settings.yml` cu configurarea globala dorita
    
    Aceasta configurare inlocuieste configurarea implicita si se va aplica global in utilizarea aplicatiei. In continuare configurarile existente in directorul curent *suprascriu configurarea globala* (se aplica cu precedenta).

>[Aici puteti gasiti pentru descarcare un model de sablon de configuare](../doc_src/downloads.md#sablon-fisier-configurare-a-aplicatiei-xl2roefact).






## Utilizare nomenclator de furnizori
Aplicatia *xl2roefact* permite utilizarea datelor pentru furnizori din fisiere externe (in locul informatiilor din fisierele Excel) lucru ce poate fi folositor in urmatoarele situatii:

* cind utilizatorul aplicatiei o face in scopuri personale si multe facturi emise il au *pe el ca furnizor*. Aceast lucru permite ca informatia din Excel referitoare la furnizor sa fie sumara sau sa lipseasca, factura finala format `PDF` fiind generata cu aplicatia
* cind utilizatorul aplicatiei o foloseste pentru a emite facturi pentru alte firme si astfel este mai comod sa foloseasca fisiere cu datele acestor firme decit sa introduca informatia in fiecare factura
* cind se doreste ca datele furnizorului sa fie preluate dintr-un sistem extern ce le poate exporta ca si fisisre


### Reguli generale de utilizare
Aceasta sectiune descrie regulile generale ce trebuiesc avute in vedere pentru o completa si corecta utilizare a facilitatii "Nomenclator furnizori":

* Nomenclatorul de furnizori se va completa intr-unul sau mai multe fisere de date (de tip text, vezi mai jos formatul exact).
* Un fisier acomodeaza un singur furnizor. Pentru mai multi furnizori se vor folosi fisiere diferite.
* Numele fisierului (fara extensie) trebuie sa coincida cu o cheie alternativa a furnizorului respectiv. Prin cheie alternativa se intelege acea cheie care este unica si poate asigura regasirea furnizorului prin folosirea ei. Ca si exemple din practicile curente ar fi cimpul numit uzual `code` sau `code_name` existent in mai toate sistemele de business. Acesta are avantajul unicitatii si a unei reprezentari "umane" (*en: human readable*). Desigur un cimp de tip cheie primara / ID este ideal dar de obicei acesta este tehnic iar valoarea sa nu ofera prea multe indicatii.
* Formatul fisierului este  [YAML](https://yaml.org/) standard, fara folosirea de modele de date complexe, aatfel incit o eventuala conversie `JSON` <--> `YAML` sa poata fi realizata manual in ambele sensuri si fara necessitatea unor cunostinte avansate ci la nivel de redefinire a numelor cheilor.


###  Locatia nomenclatorului
Fisierele cu datele furnizorilor pot sta in urmatoarele locatii:

* *directorul curent* este locatia cu prioritatea maxima si in caz de "duplicate" ale unui fisier, cel de aici va fi luat in considerare
* *directorul `data/`* din locatia unde este instalata aplicatia

Recomandari si practici uzuale:

* In situatiile in care sistemul este instalat pe un computer ce se foloseste frecvent cu aplicatia *xl2roefact* si exista un set de furnizori frecvent folositi se recomanda folosirea directorului `data/` pentru stocarea fisierelor nomenclator astfel incit sa poata fi refolosite usor.
* In situatia folosirii a "multe" fisiere date furnizori se recomanda crearea unui director dedicat in locatia utilizata (vezi mai sus) si acesta sa fie referit in numle fisierului.


### Utilizarea nomenclatorului
Pentru a folosi cu aplicatia un fisier tip nomenclator furnizor se va utiliza optiunea:
```shell
xl2roefact xl2json -o fisier_furnizor
```
unde `fisier_furnizor` este numele fisierului ce contine datele unui furnizor. Locatia acestui fisier este relativa la [locatia considerata pentru folosire](#locatia-nomenclatorului)


### Sablon pentru nomenclator de furnizori
Sablonul este proiectat pentru utilizarea in facturile emise si contine numai informatiile necesare in acest scop.<br>
Astfel cimpurile existente trebuiesc pastrate, adica nu vor fi sterse.

Vor fi *respectate si completate* corespunzator cimpurile specificate ca *obligatoriii (en: mandatory* in comentariile aferente fiecarui cimp.<br>
Pentru acele cimpuri pentru care informatia este necunoscuta sau considerata irelevanta se va completa cu `null`.

Se vor putea adauga orice alte cimpuri suplimentare cu conditia sa fie respectat formatul fisierului (`YAML`). acestea nu vor fi folosite de catre aplicatie, ci pur si simplu ignorate.

>[Aici puteti gasiti un model de sablon de configuare](../doc_src/downloads.md#sablon-fisier-cu-date-furnizor).






## Comenzile aplicatiei
Interfata aplicatie este realizata utilizind conventiile si practicile uzuale pentru aplicatii tip linie de comanda consola. Pentru informatii privind comenzile se poate folosi optiunea de **help**, dispobilia atit la nivelul general:
```shell
xl2roefact --help
```
cit si la nivel detaliat pentru fiecare comanda
```shell
xl2roefact [COMMAND] --help
```


**Lista comenzilor:**

* **about** - Afiseaza informatii despre aceatsa aplicatie (copyright, scop, etc)
* **settings** _ Afiseaza parametrii de configurare a aplicatiei. [Vezi sectiunea de configurare a aplicatiei](#configurarea-aplicatiei-xl2roefact)
* **xl2json** - Transforma fisierul (fisierele) Excel in forma JSON pentru utilizare ulterioara ca forma de date standardizat pentru schimbul de informatii cu alte sisteme electronice


**Comenzile detaliate:**

<a id="comenzile-aplicatiei"></a>  <!-- #NOTE ATTN do not drop this anchor tag because is referred in `mkdocs.yml` navigation section -->

<!--#NOTE: next section generate application commands in same style as obtained using `--help` CLI options -->
::: mkdocs-typer
    :module: xl2roefact.src.app_cli
    :command: app_cli
    :prog_name: xl2roefact
    :depth: 2





## Practici si regului referitoare la continutul facturilor din Excel
Acest capitol se refera la modul in care este "tratat" continutul fisierului Excel cu factura, mai exact la modalitatea in care informatia facturii este cautata, identificata si gasita in scopul de a fi salvata in oricare din formatele de "factura electronica / E-Fact".

Utilizarea sablonului de factura Excel ce este livrat impreuna cu aplicatia **ESTE O VARIANTA DE LUCRU RECOMANDATA**, dar nu obligatorie. Chiar si in cazul utilizarii acestuia, prin modificarea "structurii" acestuia, informatia poate ajunge *nerecognoscibila / neidentificabila* total sau partial daca nu sunt urmate regulile expuse.

>In general trebuie facuta diferenta intre datele facturii si modul in care aceasta va fi tiparita (va aparea la tiparire / previzualizare).
>
>Mai exact **continutul informational** al facturii nu trebuie nici confundat si nici mixat cu **formatul de afisare al acesteia** (layout). Pentru acesta din urma se recomanda a fi folosite cu precadere *regulile de formatare* din Excel si nu cele stocare a datelor. Un exemplu este un numar zecimal oarecare unde:
>
>* una este valoarea introdusa intr-o celula (de ex cu 3 zecimale) si
>* alta este valoarea afisata (cu 2 zecimale) - aceasta din urma trebuie obtinuta prin formatarea celulei respective de a afisa 2 zecimale prin rotunjire insa valoarea efectiva trebuie sa fie cea originala cu 3 zecimale, lucru (diferenta) care se poate vedea la editarea continutului celulei.


### Reguli recomamdate in configurarea aplicatiei pe specificul Excel al facturilor dumneavoastra

{% include './src/data/README_app_config_rules.md' %}




## Tutorial utilizare aplicatie


### Organizarea informatiei

Aplicatia *xl2roefact* "promoveaza" structurarea informatiei procesate astfel incit sa fie evitata situatia *"de aglomerare" a directorului curent cu fisiere* ce trebuiesc identificate si izolate in situatia in care se fac *procesari in masa* (pe mai multe fisiere / facturi sursa).

Astfel, aplicatia se asteapa ca fisierele Excel sursa (*adica facturile de procesat*) sa fie copiate in directorul **`invoice_files/`** de unde vor fi citite si tot aici vor fi create fisierele rezultate (JSON, XML, etc). Acest director este relativ la directorul curent de unde este lansata aplicatia si considerat *"implicit"* cu acest nume dar daca se doreste un alt director acest lucru poate fi facut folosind parametrul *`--files-directory`* (sau prescurtat *`-d`*) la lansarea aplicatiei astfel:
```bash
xl2roefact -d "calea si numele directorului dorit"
```

!!! note "Nota"
    <small markdown="1">Ghilimelele sunt necesare numai daca numele si calea (`path`) contin caracterul spatiu.</small>

**Exemple:**

* pentru stabilirea directorului curent ca sursa pentru fisierele factura Excel:
```bash
xl2roefact -d ./
```

* procesarea tuturor facturilor facturilor din luna *iunie*, copiate intr-un director dedicat sub directorul curent:
```bash
xl2roefact -d ./facturi_iunie/
```


### Exemplu de procesare a unei facturi

* se creaza directorul recomandat pentru stocarea facturilor in Excel:
```bash
md invoice_files
```

* se copiaza factura `factura_A.xlsx` in acest director apoi se revine in directorul anterior daca acesta a fost schimbat pentru efectuarea copierii

* se lanseaza aplicatia:
```bash
xl2roefact xl2json
```

In urma acestor operatii, in directorul `invoice_files` vor rezulta:

```tree
invoice_files/
    factura_A.xlsx  # fisierul Excel original
    factura_A.json  # fisierul JSON rezultat in urma procesarii
```

* `factura_A.xlsx` ca fiind fisierul Excel original cu factura
* `factura_A.json` acesta fiind fisierul format JSON rezultat in urma procesarii si ce poate fi folosit pentru interschimbarea electronica a informatiei intre sisteme





## Aspecte tehnice referitoare la formatul fisierului JSON aferent facturii

Acest fisier este cel generat de catre aplicatie in urma executiei acesteia cu comanda `xl2json`. Formatul JSON are urmatoarra structura de baza:

```json
{
    "Invoice": {...},
    "meta_info": {...},
    "excel_original_data": {...}
}

```

Cheile de la primul nivel contin:

* **`Invoice`** - datele efective ale facturii
* **`meta_info`**
    * informatii referitoare la procesarea facturii si mapa de conversie a cheii `Invoice` din formatul `JSON` in formatul `XML` cerut de sistemul *RO E-Fact*
    * harta de ajutor in conversia formatului JSON in formatul XML acceptat de sistemul RO E-Fact (cheie `meta_info.map_JSONkeys_XMLtags`) si definititiile XML aferente (cheie `meta_info.invoice_XML_schemes`)
    * alte informatii despre fisierul Excel prelucrat (numele, worksheet cu factura, data si ora procesarii, CRC pentru verificare, etc)
* **`excel_original_data`** - informatiile originale din fisierul Excel, asa cum au fost ele identificate si gasite precum si locatia (adresele celulelor). Aceste informatii sunt utile in cazul in care exista neclaritati in urma procesuluicde conversie pentru "a intelege" de unde si cum arata informatiile originale din fisierul Excel

Detalii suplimentare despre formatul JSON se gasesc in documentaţia *[Referinta dezvoltare software](./doc/README_xl2roefact_library.md)*.




## Descarcare (download) aplicatie xl2roefact CLI

* [Pachet instalare aplicatie Windows](../doc_src/downloads.md#format-executabil-windows-x64)
* [Pachet instalare script Python](../doc_src/downloads.md#format-biblioteca-python)
* [Model de sablon de configuare](../doc_src/downloads.md#sablon-fisier-configurare-a-aplicatiei-xl2roefact)
* [Sablon fisier-date informatii furnizor](../doc_src/downloads.md#sablon-fisier-cu-date-furnizor)




## Referinta dezvoltare software

Documentatia **["Referinta dezvoltare software"](./doc/README_xl2roefact_library.md)** ofera detail necesare pentru utilizarea bibliotecii sursa in dezvoltari specifice, extindere si integrare cu alte sisteme.




## Date identificare

* part number (p/n): `0000-0095-xl2roefact`
* producator si copyright: RENWare Software Systems (referinte detalii tehnice: Petre Iordanescu, *petre.iordanescu@gmail.com*)




## [License](./LICENSE "download")






## Note

[^ld_roefact]: Toate interactiunile cu sistemul *ANAF RO E-Fact* necesita o *conexiune la internet* si un set de *credentiale ANAF RO E-Fact ale companiei* pentru care se incarca factura. In lipsa acestora, fisierul `XML` generat de aplicatie poate fi incarcat ulterior (de ex de catre departmentul contabilitate)


