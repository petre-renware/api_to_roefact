<small>**RENware Software Systems**</small>





# Propunere tehnica sistem payments_validation_board

* p/n: `0000-0094`
* code-name: `payments_validation_board`
* commercial name: **PayValBo**
* url propunere tehnica: `http://api_to_roefact.renware.eu/commercial_agreement/110-SRE-payments_validation_board_req.uirements.html`
* git: `n/a`

***Cuprins:***

[TOC]





## Obiective

Acest sistem asigura prezentarea unui "_dashboard_" cu lista facturilor primite si starea lor de **verificare si aprobare interna** in vederea ordonantarii lor la plata.







## Vedere de ansamblu a solutiei

Sistemul `payments_validation_board` consta din urmatoarele componente:

* `payments_validation_board`.**`INV_BRD`** - aceasta componenta prezinta **pentru MANAGEMNTul tip CFO** lista facturilor primite si starea lor referitor la validarea si aprobarea lor si un control pentru *APROBARE FINALA sau BUN DE PATA*. <!--#TODO wip... -->

* `payments_validation_board`.**`INV_CHK`** - aceasta componenta prezinta **pentru VERIFICATORI si APROBABTORI** lista facturilor primite si diverse controale pentru aprobarea si scrierea de diverse note si observatii. <!--#TODO wip... -->

* `payments_validation_board`.**`INV_NOTIF`** aceasta componenta prezinta notificari referitoare la **diversele OBSERVATII si NOTE** facture asupra facturilor primite in diverse stadii de aprobare de catre persoanele care efectueaza verificari asupra lor (prin componenta `INV_CHK`). Notificarile sunt disponibile atit in interfata aplicatiei iar *unele din ele pot fi transmise prin mail*. <!--#TODO wip... -->


...IN PROGRESS... ![wip-picture](../pictures/under_maintenance.png){ width="150" } <!--#TODO -->




## Cerinte functionale generale

...INCOMING... ![wip-picture](../pictures/under_maintenance.png){ width="150" } <!--#TODO -->



## Componenta xxx

...INCOMING... ![wip-picture](../pictures/under_maintenance.png){ width="150" } <!--#TODO -->








