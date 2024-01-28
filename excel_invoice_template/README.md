<small markdown=1>Copyright (C) **RENware Software Systems**</small>

[TOC]

# invoice template


## Instalarea sablonului de factura emisa

Aceasta componenta consta dintr-un director (ce nu necesita instalare speciala ci simpla copiere locala acolo unde va fi utilizat). Acest director contine:

* fisierul pentru factura `invoice_template_CU_tva.xlsx` ce este disponibil pentru [descarcare aici](./invoice_template_CU_tva.xlsx "download")

* directorul `released_packages/` ce contine versiuni anterioare de sablon ce sunt inca suportate

* prezentul document




## Recomandari in utilizarea sablonului

Aceasta sectiune se refera la modul in care ar trebui "tratat" continutul fisierului Excel cu factura ***in conditiile in care se intentioneaza ca aceasta sa fi procesata ulterior cu sistemul `INVOICEtoROeFact`***. Acest sablon este general valabil (este un fisier Excel ca oricare altul) deci in acest caz este important a "constientiza" faptul ca informatia aferenta facturii din Excel va fi cautata, identificata si gasita in scopul de a fi salvata in formatele de factura electronica (utilizarea acestui sablon de factura Excel impreuna cu sistemul `INVOICEtoROeFact` **ESTE O VARIANTA DE LUCRU RECOMANDATA**, dar nu obligatorie).

Astfel **se recomanda ca acest sablon sa fie utilizat asa cum este livrat**, fara a efectua modificari majore in structura sa cum ar fi:

* modificarea formatelor (de tip de date) celulelor in scopul unei afisari "mai frumoase"

* adaugarea de informatii prin concatenare de siruri de caractere sau orice alte metode de a altera continutul vizibil al celulelor in scopul unei afisari "mai frumoase"

* modificarea locatiilor celulelor prin inserarea sau stergerea de linii, coloane sau celule noi

>**In general trebuie facuta diferenta intre datele facturii si modul in care aceasta va fi tiparita (va aparea la tiparire / previzualizare).**




<small markdown="1">

DETALII TEHNICE:

Continutul informational al facturii nu trebuie nici confundat si nici mixat cu **formatul de afisare al acesteia** (layout). Pentru acesta din urma se recomanda a fi folosite cu precadere *regulile de formatare* din Excel si nu cele stocare a datelor. Un exemplu este un numar zecimal oarecare unde:

* una este valoarea introdusa intr-o celula (de ex cu 3 zecimale) si
* alta este valoarea afisata (cu 2 zecimale) - aceasta din urma trebuie obtinuta prin formatarea celulei respective de a afisa 2 zecimale prin rotunjire insa valoarea efectiva trebuie sa fie cea originala cu 3 zecimale, lucru (diferenta) care se poate vedea la editarea continutului celulei.

</small>
