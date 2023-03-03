import requests

url = "http://web-02.challs.olicyber.it/server-records"
params = {"id": "flag"}

response = requests.get(url, params=params)

print(response.text)

# ____________________________________________________________________ # 
#  Il codice utilizza la funzione "get" di "requests" per inviare una 
#  richiesta GET al server con la risorsa desiderata e il parametro 
#  "id" impostato su "flag". 
#  La risposta del server viene memorizzata nell'oggetto "response" 
#  e il contenuto della risposta viene stampato 
#  sulla console utilizzando la proprietà "text" dell'oggetto 
#  "response".
# ____________________________________________________________________ #

# FLAG ==> flag{wh47_i5_y0ur_qu3ry}