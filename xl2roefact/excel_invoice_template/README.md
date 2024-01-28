<small markdown=1>**Copyright (C) RENware Software Solution**</small>

[TOC]

# invoice template


## Instalarea sablonului de factura emisa

Aceasta componenta consta dintr-un director (ce nu necesita instalare speciala ci simpla copiere locala acolo unde va fi utilizat). Acest director contine:

* fisierul pentru factura `invoice_template_CU_tva.xlsx` ce este disponibil pentru [descarcare aici](./excel_invoice_template/invoice_template_CU_tva.xlsx)

* directorul `released_packages/` ce contine versiuni anterioare de sablon ce sunt inca suportate

* prezentul document




## Recomandari in utilizarea sablonului

![wip-picture](../doc_src/pictures/under_maintenance.png){ width="150" } <!--#TODO -->
... Sectiune in lucru ...


<!--NOTE: aceasta sectiune este preluata din README `xl2roefact` -->
Aceasta sectiune se refera la modul in care ar trebui "tratat" continutul fisierului Excel cu factura ***in conditiile in care se intentioneaza ca aceasta sa fi procesata ulterior cu sistemul `INVOICEtoROeFACT`***. , mai exact la modalitatea in care informatia facturii este cautata, identificata si gasita in scopul de a fi salvata in oricare din formatele de "factura electronica / E-Fact".

Utilizarea sablonului de factura Excel ce este livrat impreuna cu aplicatia **ESTE O VARIANTA DE LUCRU RECOMANDATA**, dar nu obligatorie. Chiar si in cazul utilizarii acestuia, prin modificarea "structurii" acestuia, informatia poate ajunge *nerecognoscibila / neidentificabila* total sau partial daca nu sunt urmate regulile expuse.

>In general trebuie facuta diferenta intre datele facturii si modul in care aceasta va fi tiparita (va aparea la tiparire / previzualizare).
>
>Mai exact **continutul informational** al facturii nu trebuie nici confundat si nici mixat cu **formatul de afisare al acesteia** (layout). Pentru acesta din urma se recomanda a fi folosite cu precadere *regulile de formatare* din Excel si nu cele stocare a datelor. Un exemplu este un numar zecimal oarecare unde:
>
>* una este valoarea introdusa intr-o celula (de ex cu 3 zecimale) si
>* alta este valoarea afisata (cu 2 zecimale) - aceasta din urma trebuie obtinuta prin formatarea celulei respective de a afisa 2 zecimale prin rotunjire insa valoarea efectiva trebuie sa fie cea originala cu 3 zecimale, lucru (diferenta) care se poate vedea la editarea continutului celulei.


<!--#TODO: copy rules used in `rdinv()` module to corectly recognize Excel data and make JSON invoice file
-->




## 

