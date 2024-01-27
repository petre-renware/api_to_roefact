s<small>**RENware Software Systems**</small>

# Optiuni tehnice

***Cuprins:***

[TOC]





Acest document prezinta posibilele optiuni tehnice la cele doua sisteme, optiuni care vor trebui agreate si (preferabil) planificate cel putin din punct de vedere al prioritatii.


## Optiuni sistem INVOICEtoROefact

!!! example "Forma de utilizare si interactionare"
    - &#x2610; (**INVOICEtoROefact-RQ-01**) -
    varianta CLI (command line) cu utilizare "individuala"
    - &#x2610; (**INVOICEtoROefact-RQ-02**) -
    varianta WEB cu utilizare centralizata


!!! example "Configurabilitate"
    - &#x2610; (**INVOICEtoROefact-RQ-03**) -
    varianta in care se prelucreaza un model de fisier `Excel` in care sunt "fixate si blocate" locatiile celulelor ce contin date relevante
    - &#x2610; (**INVOICEtoROefact-RQ-04**) -
    varianta in care structura si formatul fisierului `Excel` contin "cuvinte cheie" ce determina regasirea date relevante (de exemplu textul "Client:" intr-o celula semnifica inceperea unei zone cu datele clientului de la acea celula in jos si pina prima celula necompletata ce va fi gasita)



### Recomandari sistem INVOICEtoROefact

* varianta (INVOICEtoROefact-RQ-01) este recomandata ca fiind "aproape obligatorie" deoarece chiar si in varianta WEB ea va trebui scrisa intr-o forma neutilizabila direct (sub forma de functie a sistemlui). Transformarea acestei functii in varianta CLI va permite o executie portabila ("la purtator") si offline (in situatii extreme se poate folosi doar fisierul `XML` generat si acesta va putea fi manual incarcat in ANAF-SPV). Informatia privind "starea de incarcare a facturii" va fi oricum salvata si in fisierul Excel aferent facturii si va putea fi preluata de catre varianta WEB pentru centralizarea informatiilor- a se vedea si [modulul `LDXML` si notele de subsol aferente](110-SRE-api_to_roefact_requirements.md#componenta-xl2roefact)

* optiunea (INVOICEtoROefact-RQ-03) este recomandata ca varianta de start deoarece va permite realizarea unei variante OPERATIONALE (de lucru curent si testare) intr-un termen mai scurt, urmind ca aceasta optiune sa fie gradat extinsa si cu optiunea (INVOICEtoROefact-RQ-04). Aceasta "linie de lucru" nu va induce probleme, avind in vedere ca orice optiune / varianta aleasa ca varianta de start si planificata a fi extinsa va implica si MIGRAREA datelor deja produse la momentul extinderii ei






## Optiuni sistem PayValidaBoa

!!! example "Framework standardizat de orchestrare"
    - &#x2610; (**PayValidaBoa-RQ-01**) - utilizarea unui framework specializat de orchestrare si integrare cu alte sisteme "externe"
        * *Implicatii:* poate mari durata de implementare
        * *Avantaje:* utilizarea ulterioara pentru integrare intre sisteme ce prezita interfata standardizata (REST, SOA, NTFS, EXT4, OAuth, ...)


!!! example "Semnare electronica a facturilor verificate"
    - &#x2610; (**PayValidaBoa-RQ-02**) - utilizarea de certificat tip "semnatura electronica" pentru autentificarea verificarii facturilor *EMBEDDED IN FACTURA*
    - &#x2610; (**PayValidaBoa-RQ-03**) - utilizarea de certificat tip "semnatura electronica" pentru autentificarea verificarii facturilor *adiacet facturii - disponibil pentru consultare numai in sistemul PayValidaBoa*
    - &#x2610; (**PayValidaBoa-RQ-04**) - verificarea facturilor nu necesita certificat tip "semnatura electronica" ci simpla informatie existenta in sistemul PayValidaBoa este suficienta


!!! example "Baza de date 'interna / specifica' sistemului PayValidaBoa"
    - a se vedea [documentul *"Considerente tehnice generale"*, sectiunea *"Considerente generale privind bazele de date proprii sistemelor"*, item *"(DBS-03)"*](110-SRE-general_requirements.md#considerente-generale-privind-bazele-de-date-proprii-sistemelor) pentru opptiuni privind baza de date ce va fi utilizata "pentru operatiuni interne si specifice" de catre sistemul PayValidaBoa









## Optiuni generale de implementare

!!! example "Sistemele tip infrastructura ce vor fi utilizate"
    - &#x2610; (**general-RQ-01**) - server web-HTTP pentru aplicatiile de tip WEB (*ATENTIE:* sistemele WEB ce vor fi implementate necesita interfata / mod de operare standard `WSGI`)
    - &#x2610; (**general-RQ-02**) - sistem de autentificare utilizat (intern aplicatie, Google, Identity Management propriu, ...)
    - &#x2610; (**general-RQ-03**) - sistemele vor rula pe infrastructura proprie sau aceastea vor rula in infrastructuri gazduite


!!! example "Alte optiuni 'ad-hoc' (in sedinta)"
    - ...
    - ...
    - ...
    - ...
    - ...
    - ...






<!--#NOTE special HTML characters to use:
    - &#x2610; checkbox as NOT CHECKED
    - &#x2611; checkbox as CHECKED
-->

