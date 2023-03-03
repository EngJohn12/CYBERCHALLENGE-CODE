import requests

url = 'http://web-08.challs.olicyber.it/login'
data = {'username': 'admin', 'password': 'admin'}
response = requests.post(url, data=data)
print(response.text)




#___________________________________________________________________________________#
# In questo codice si importa la libreria requests, si definisce l'URL di destinazione 
# della richiesta POST, e si crea un dizionario contenente i 
# valori "username" e "password". 
# Questo dizionario viene passato al parametro data della funzione post di requests, 
# che si occupa di generare automaticamente il formato application/x-www-form-urlencoded
# a partire dal dizionario. La risposta viene infine stampata a video tramite 
# response.text.
 
# FLAG ==> flag{53nding_d474_7h3_01d_w4y}
