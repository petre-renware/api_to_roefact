<small>**RENware Software Systems**</small>





# Propunere tehnica sistem PayValidaBoa

* p/n: `0000-0094`
* code-name: `payments_validation_board`
* commercial name: **PayValidaBoa**
* url propunere tehnica: `http://apitoroefact.renware.eu/commercial_agreement/110-SRE-payments_validation_board_req.uirements.html`
* git: `n/a`

***Cuprins:***

[TOC]





## Obiective

Acest sistem asigura prezentarea unui "_dashboard_" cu lista facturilor primite si starea lor de **verificare si aprobare interna** in vederea ordonantarii lor la plata.







## Vedere de ansamblu a solutiei

Sistemul `payments_validation_board` consta din urmatoarele componente:

* `payments_validation_board`.**`INV_BRD`** - aceasta componenta prezinta ***pentru MANAGEMNTul tip CFO*** lista facturilor primite si starea lor referitor la **validarea si aprobarea lor finala** si un control pentru *APROBARE FINALA sau BUN DE PATA*. <!--#TODO wip... -->

* `payments_validation_board`.**`INV_CHK`** - aceasta componenta prezinta ***pentru VERIFICATORI si APROBABTORI*** lista facturilor primite si **diverse controale pentru aprobarea si scrierea de diverse note** si observatii. <!--#TODO wip... -->

* `payments_validation_board`.**`INV_NOTIF`** aceasta componenta prezinta notificari referitoare la **diversele OBSERVATII si NOTE** facture asupra facturilor primite in diverse stadii de aprobare de catre persoanele care efectueaza verificari asupra lor (prin componenta `INV_CHK`). Notificarile sunt disponibile atit in interfata aplicatiei iar *unele din ele pot fi transmise prin mail*. <!--#TODO wip... -->

* `payments_validation_board`.**`ADMIN_CFG`** aceasta componenta permite ***pentru ADMINISTRATORI*** diverse **OPTIUNI DE CONFIGURARE**:
    * lista utilizatorilor ce fac parte dinfluxul de aprobare
    * adresele e-mail ale utilizatorilor
    * rolul utilizatorilor in accea ce priveste fluxul de aprobare facturile primite
    * certificate si semnaturile de certificare a "semnaturilor" de aprobare
    * ... <!--#TODO wip... -->


Figura urmatoare prezinta schematic rolul general al componentelor precum si interactiunea acestora cu mediul exterior sistemului `payments_validation_board`.

<!--#NOTE_update_me ![arh-api_to_roefact](../pictures/api_to_roefact_architecture.png) --> <!--#TODO -->

...IN PROGRESS... ![wip-picture](../pictures/under_maintenance.png){ width="150" } <!--#TODO -->




## Cerinte functionale generale

...INCOMING... ![wip-picture](../pictures/under_maintenance.png){ width="150" } <!--#TODO -->



## Componenta xxx

...INCOMING... ![wip-picture](../pictures/under_maintenance.png){ width="150" } <!--#TODO -->








