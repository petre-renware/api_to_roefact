# draft lucru mapa JSON - XML

--- #TODO: a se sterge la final...

Format sintaxa: `JSON -> XML @ invoice_header_area["customer_area"][...]`


* cac_Contact  ->  cac:Contact  @  ...n/a... *Part of `<cac:Party>` XML tag/key*
    * cbc_Telephone  ->  cbc:Telephone  @  ["phone"]
    * cbc_ElectronicMail  ->  cbc:ElectronicMail  @  ["email"]

* RegCom  -->  ...n/a...  @  ["reg_com"] 

* Bank  -->  ...n/a...  @  ["bank"] 

* IBAN  -->  ...n/a...  @  ["IBAN"] 


### Alte key in JSON "Invoice" ce nu sunt in schema XML that si care trebuie trecute in *map structure* key `"map_JSONkeys_XMLtags"` pentru ca au fost uitate

* LineVatAmount  -->  ...n/a...



