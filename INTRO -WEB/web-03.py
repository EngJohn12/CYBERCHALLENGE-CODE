import requests

url = "http://web-03.challs.olicyber.it/flag"
headers = {"X-Password": "admin"}

response = requests.get(url, headers=headers)

print(response.text)

#_________________________________________________________#
# Il codice utilizza la funzione "get" di "requests" 
# per inviare una richiesta GET al server con la risorsa 
# desiderata e l'header "X-Password" impostato su "admin". 
# La risposta del server viene memorizzata nell'oggetto 
# "response" e il contenuto della risposta viene stampato 
# sulla console utilizzando la proprietà "text" 
# dell'oggetto "response".
#__________________________________________________________#

 # FLAG ==> flag{7ru57_m3_i_m_7h3_4dmin}

