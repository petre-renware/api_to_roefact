""" CHKISLD - modul de verificare a starii de incarcare a unei facturi emise
Identification:
    code-name: `chkisld`
    copyright: (c) 2023 RENWare Software Systems
    author: Petre Iordanescu (petre.iordanescu@gmail.com)
Deploymens:
    all op sys: Python library
Specifications:
    document: `110-SRE-api_to_roefact_requirements.md` section `Componenta BASE_PROC`
    INTRARI: fisier `f-XLSX` sau numarul / cheia / codul facturii
    IESIRI: valoarea echivalent `TRUE` daca factura a fost deja incarcata sau valoare echivalent `FALSE` daca factura nu a fost incarcata
"""





import typer


