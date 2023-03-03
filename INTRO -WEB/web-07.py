import requests

url = "http://web-07.challs.olicyber.it/"
response = requests.head(url)
print(response.headers)

#_______________________________________________________________#
# La funzione head invia una richiesta HTTP HEAD all'URL 
# specificato e restituisce un oggetto Response che contiene 
# gli header della risposta. Nel codice sopra, gli header sono 
# stampati a schermo attraverso la proprietà headers dell'oggetto 
# Response.



#FLAG ==> flag{r0gu3_m374d474}