![api_to_roefact_logo](pictures/api_to_roefact_logo.png){ width="300" }


<!-- #NOTE -- TEST HTML FORM ------------------------------------------------
---pui un div cu markdown ? Better...
<form action="XXX_TEST_ROUTE/xxxfile">
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname" value="John"><br>

  <label for="lname">Last name:</label>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form>

# Note si explicatii rezultat:

    - caz 0: util acces **`booklab_app`**: `<form method="POST" action="http://localhost:5000">` unde 5000 este portul ales

    - caz 1: cu `action="/XXX_TEST_ROUTE"` ==> raspunsul a fost request catre `/XXX_TEST_ROUTE?fname=John&lname=Doe` url ABSOLUT

    - caz 2: cu `action="XXX_TEST_ROUTE"` ==> raspunsul a fost request catre `http://server_name.../XXX_TEST_ROUTE?fname=John&lname=Doe` url RELATIV la servername

    - caz 3: cu `action="XXX_TEST_ROUTE/xxxfile"` ==> raspunsul a fost request catre `http://server_name.../XXX_TEST_ROUTE/xxxfile?fname=John&lname=Doe` url RELATIV la servername

------------------------------------------------------------------------->




# APItoROefact

<small markdown="1">by RENware Software Systems</small>

Welcome to **APItoROefact** world, your personal assistant in putting your ideas in practice and making your books as you dreamed them.

Bine ai venit in lunea **APItoROefact**, asistentul tau personal in punerea ideilor tale in practica si realizarea cartlior si materialelor tale asa cum le-ai visat.


Ce poti face mai departe:

* **[sa vezi catalogul cartilor tale](bcat/)** #TODO BCAT route

* **[sa incepi o noua carte](newb/)** #TODO NEWB route

* **[sa creezi si sa editezi continutului unui material](edtm/)** #TODO EDTM route

* **[sa organizezi materialele in diverse sectiuni](orgm/)** #TODO 0RGM route

* **[sa vizualizezi si sa testezi materiale realizate](prvb/)** #TODO PRVB route

* **[sa faci asamblarea finala a cartii in forma electronica](dplb/)** #TODO DPLB route


Daca inca nu esti sigur sau hotarit, poti sa revezi doumentatia sistemului:

* **[sa citesti "Vederea de ansamblu" a APItoROefact](help/130.02-Overview.md){ target="_blank" }**

* **[sa revezi manualele de utilizare](help/880.30-EUMA_catalog.md){ target="_blank" }**

* **[sa revezi manualele de configurare](help/880.30-ADMA_catalog.md){ target="_blank" }**




