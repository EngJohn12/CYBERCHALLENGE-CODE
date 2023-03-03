import requests
from bs4 import BeautifulSoup

url = 'http://web-13.challs.olicyber.it/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

flag = ''
for tag in soup.find_all():
    if tag.text.isalpha():
        flag += tag.text

print('Flag:', 'flag{' + flag + '}')
   #_______________________________________________________________________________#
   # In questo codice, la funzione requests.get() viene utilizzata per ottenere il 
   # contenuto della pagina web all'indirizzo specificato dall'URL. 
   # La libreria BeautifulSoup viene poi utilizzata per analizzare il contenuto 
   # HTML della pagina e trovare tutti i tag presenti al suo interno.
   # Per ogni tag trovato, verifichiamo se il suo testo contiene solo lettere 
   # attraverso il metodo isalpha(). Se il testo del tag è composto solo da lettere, 
   # lo aggiungiamo alla variabile flag. Infine, concateniamo la stringa 
   # "flag{" all'inizio della variabile flag e la cornice "}" alla fine per ottenere 
   # la flag completa.

# FLAG ==> flag{donotrecommenddoingthisbyhand}