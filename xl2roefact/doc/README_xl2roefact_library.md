<!-- NOTE:
- This is the general technical design for `xl2roefact python library` component
- The DLD doc is a tech desc of every module, functions
-->


# Software development reference using xl2roefact python library

[TOC]



## Library components

### Basic processing components
These components assure the basic elementary-raw processing of information. Their interface is pure technical and require basic development knowledge to be used "as is".

* `rdinv` read an Excel file and extract invoice data to a JSON file format
* `wrxml`  write, convert the JSON invoice file to a XML file format, respecting schemes required by *RO EFact* standard
* `chkxml` check generated XML file
* `ldxml` load an invoice (ie, its XML associated file) to *ANAF SPV system*
* `chkisld` check if an invoice is already loaded in *ANAF SPV system*

### Configuration components
These are the components that assure and make possible system configurablitity at user level.

* `config_settings` *USER level* configuration - define application settings & parameters mainly used in invoice info / data detection and extract from invoice Excel format file
* `sys_settings` *SYSTEM level* configuration - system database and parameters, not changeable at user level in current application usage (changing these parameters needs code updating to make them effective) - details in section [Sysyem database and parameters](#sysyem-database-and-parameters)

### Presentation components
These components are high level layers that make sysyem usable in various forms such as command line console application, daemon / server that runs in background and can be called from local or remote clients, library interfaces (for extensions and custom development) that hide low level technical execution details.

* `app_cli` contains the code for `xl2roefact` application command line (CLI) format
* `__main__` assures right package "addressing" as Python modele (ie, running as `python -m xl2roefact ...`)
* `__version__` keeps current system version and helper functions to assure standard and canonical representation of version string
* `__init__` assure friendly exposing of system public objects (and of course classic pytgon role of "package maker")




## Install library
Library can be installed using 2 methods:

* install from PyPi
* install from site archive of distribution packages

### Install from PyPi
The library installation can be done using standard Python instruments:

```bash
pip install xl2roefact
```

This command will install by default the last stable version. For other versions, standard PyPi procedure to  install a specific version must be used.


### Install from distribution packages
To install from distribution packages first download the package version intended to install ([see download section](#download-xl2roefact-library)), choose the package type (if you have no special option, then choose *`WHEEL`* format) and install it using `pip` as any other Python library installation (*detailed in Python official documentation*).





## Aspecte tehnice referitoare la formatul fisierului JSON aferent facturii
Acest fisier este cel generat de catre aplicatie in urma executiei acesteia cu comanda `xl2json`. Structura de baza a acestui fisier este:


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


An [example of JSON generated file is available here](./invoice_json_model_.md)




## Sysyem database and parameters
System database is an object that interface library components with physical stores of parameters and data requred by system and its applications.

Sometimes it can contain both physical and logical interfaces one example being *InvoiceTypes*  which consists of:

* `InvoiceTypes: dict` the physical store of invoice types name and codes
* `InvoiceTypesEnum: Enum` the logical object with invoice types implemented as standard Python enumeration (`enum`)

This let open the possibility that in future versions to "externalize" physical data-objects to other systems or distinct files, but letting small / tinny physical data-objects to stay in `sys_settings.py` module.




## [API Refrence](https://invoicetoroefact.renware.eu/xl2roefact/doc/wrapper_810.05a-xl2roefact_DLD_specs.html)

<!--NOTE: reference using in-profect document
[API Reference](./wrapper_810.05a-xl2roefact_DLD_specs.md)
-->




## Download xl2roefact library

* [Pachete instalare biblioteca Python formate WHEEL si DIST](../../doc_src/downloads.md#format-biblioteca-python)









