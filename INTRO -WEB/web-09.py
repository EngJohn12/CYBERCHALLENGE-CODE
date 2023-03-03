import requests

url = 'http://web-09.challs.olicyber.it/login'
data = {'username': 'admin', 'password': 'admin'}
response = requests.post(url, json=data)
print(response.text)


#____________________________________________________________#
#Per inviare la richiesta POST con body codificato in JSON si 
# può utilizzare la libreria requests di Python e la funzione 
# post, passando il parametro json invece di data. In questo modo, 
# si può passare un dizionario Python contenente le coppie 
# chiave-valore da inviare, e requests si occuperà di codificare 
# automaticamente il body in formato JSON.