import requests

url = "http://web-04.challs.olicyber.it/users"
headers = {"Accept": "application/xml"}
response = requests.get(url, headers=headers)

print(response.text)


#________________________________________________________________# 
# In questo codice, stiamo utilizzando la funzione 
# get della libreria requests per inviare una richiesta GET 
# all'URL specificato. Stiamo inoltre specificando un header 
# personalizzato chiamato Accept con il valore "application/xml" 
# per indicare che vogliamo ricevere la risorsa in 
# formato XML anziché in formato JSON.
#Infine, stiamo stampando la risposta ricevuta dal server 
# tramite l'attributo text dell'oggetto Response restituito 
# dalla funzione get.

#________________________________________________________________# 


# FLAG ==> flag{54m3_7hing_diff3r3n7_7hing}
