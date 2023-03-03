import requests

url = 'http://web-05.challs.olicyber.it/flag'
cookies = {'password': 'admin'}
response = requests.get(url, cookies=cookies)

#_____________________________________________________________#
# 
# In questo caso si utilizza il parametro cookies della 
# funzione get() per includere il cookie password=admin nella 
# richiesta HTTP. Il server risponderà solo se il cookie 
# password ha il valore admin. Il contenuto della risposta, 
# che dovrebbe includere 
# la flag cercata, viene quindi stampato sulla console.
#_____________________________________________________________#


# FLAG ==> flag{v3ry_7457y_c00ki35}