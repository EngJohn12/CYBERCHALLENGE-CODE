import requests

# Istanziamo un oggetto Session
session = requests.Session()

# Eseguiamo la richiesta GET a http://web-06.challs.olicyber.it/token
response = session.get('http://web-06.challs.olicyber.it/token')

# Otteniamo il valore del cookie dalla risposta
cookie_value = response.cookies.get('session')

# Prepariamo il cookie da inviare nella richiesta successiva
cookie = {'session': cookie_value}

# Eseguiamo la richiesta GET a http://web-06.challs.olicyber.it/flag con il cookie
response = session.get('http://web-06.challs.olicyber.it/flag', cookies=cookie)

# Stampiamo il contenuto della risposta
print(response.text)


#____________________________________________________________________#
# inizializziamo un oggetto di classe Session e lo assegniamo alla 
# variabile session. Successivamente, eseguiamo una richiesta GET 
# a http://web-06.challs.olicyber.it/token utilizzando il metodo get 
# dell'oggetto session e salviamo la risposta nella variabile response.
# Per ottenere il valore del cookie di sessione dalla risposta, 
# utilizziamo il metodo get dell'attributo cookies della risposta 
# response passando come argomento il nome del cookie ("session").
# Successivamente, prepariamo il cookie da inviare nella richiesta 
# successiva come un dizionario con chiave "session" e valore il
#  valore del cookie ottenuto precedentemente.
# Infine, eseguiamo una richiesta GET a 
# http://web-06.challs.olicyber.it/flag utilizzando ancora 
# il metodo get dell'oggetto session, passando come argomento l'URL 
# della risorsa e il cookie precedentemente preparato come parametro cookies. 
# La risposta viene salvata nella variabile response.
# Infine, stampiamo il contenuto della risposta utilizzando l'attributo 
# text della variabile response.

# FLAG ==> flag{7w0_574g3_4cc3s5}


