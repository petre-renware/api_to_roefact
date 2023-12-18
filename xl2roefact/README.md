
[TOC]

# xl2roefact | xl-invoices

Excel invoice creation, generate JSON, XML, PDF and upload to RO E-Fact system.

* Components
    * **`xl2roefact`** command line application to create, manipulate and upload to RO E-Fact system Excel invoices
    * **`xl-invoices`** Python library to use functions to create, manipulate and upload to RO E-Fact system Excel invoices

* Identification
    - code-name: `xl2roefact`
    - copyright: (c) 2023 RENWare Software Systems
    - author: Petre Iordanescu (petre.iordanescu@gmail.com)

* Deployments
    - Windows: `xl2roefact.exe` deployable by `MSI` package portable 64 bit CLI application
    - Linux: `xl2roefact` executable CLI shell

* Specifications
    - command general format: `xl2roefact [COMMAND] [OPTIONS]`
    - help: `xl2roefact [COMMAND] --help`




## Instalarea

Acest sistem consta din doua componente:

- o aplicatie de tip *linie de comanda consola* ce permite realizarea operatiilor necesare de procesare a facturilor in Excel (**`xl2roefact`** CLI application)
- o biblioteca (**`xl_invoices`**) ce permite utilizarea functionalitatilor de procesare a facturilor in Excel in mod programatic prin inglobarea acesteia in alt cod si utilizarea ei corespunzatoare.  Biblioteca este realizata in Python 3 iar instalarea ei se poate face cu instrumentele standard Python



### Instalarea aplicatiei xl2roefact

Pachetele de instalare se gasesc in directorul `dist/` ca arhive `ZIP`. Pachetele disponibile contin in numele lor versiunea de aplicatie utilizata si versiunea sistemului de operare pentru care sunt disponibile.  (_EN: Installation package is found in `dist/` directory in archive (zip) files. Available packages are identified by released versions and operating systems._)

Pachetele contin un script de instalare sub forma standard `MSI` pentru Windows si `DEB` pentru Linux Debian (verificati disponibilitatea pentru sistemul de operare folosit de dvs).  (_EN: Packages contains an installation script as `MSI` for Windows and `DEB` for Debian Linux based systems (check availability for your operating system)_).


### Instalarea bliotecii xl-invoices

Instalarea acesteia se face cu instrumentele standard Python. Recomandarea este pentru instalarea simpla cu: `pip install xl-invoices`, biblioteca fiind disponibila in repositori-ul standard *PyPy*. Pentru instalarea din surse, biblioteca poate fi descarcata din [*GitHub*](https://github.com/petre-renware/api_to_roefact/tree/development/xl2roefact/xl_invoices).




## Configurarea aplicatieii xl2roefact

Parametrii de configurare a plicatiei se gasesc in fisierul **`config_settings.py`**. Acestia sunt sub elaborati in limbaj Python prin utilizarea conventiilor de constante conform recomandarilor PEP (numele capitatlizat) si sunt acompaniti de linii de explicatii privind aplicabilitatea lor.  (_EN: Configuration parameters are placed in file **`config_settings.py`**. These are in Python form presented using constants PEP recommendations (all upper case) and accompanied by some help lines to understand and maintain them)_.




## Comenzile aplicatiei

Interfata aplicatie este realizata utilizind conventiile si practicile uzuale pentru aplicatii tip linie de comanda consola. Pentru informatii privind comenzile se poate folosi optiunea de **help**, dispobilia atit la nivelul general: `xl2roefact --help`, cit si la nivel detaliat penrtur fiecare comanda: `xl2roefact [COMANDA] --help`.


### about

Afiseaza informatii despre aceatsa aplicatie (copyright, scop, etc).


### settings

Afiseaza parametrii de configurare a aplicatiei. [Vezi sectiunea de configurare](#configuration--settings)


### xl2json

Transforma fisierul (fisierele) Excel in forma JSON pentru utilizare ulterioara ca forma de date standardizat pentru schimbul de informatii cu alte sisteme electronice. Formatul JSON utilizat contine:

- informatiile aferente facturii (cheie: `Invoice`)
- o harta de ajutor in conversia formatului JSON in formatul XML acceptat de sistemul RO E-Fact (cheie `meta_info.map_JSONkeys_XMLtags`) si definititiile XML aferente (cheie `meta_info.invoice_XML_schemes`)
- alte informatii despre fisierul Excel prelucrat (alte chei din `meta_info`)
- datele preluate din formatul original Excel (cheie `excel_original_data`) - acestea sunt utile pentru depanare in caz ca aceasta este necesara in cazul specific al fisierului Excel folosit de dvs






