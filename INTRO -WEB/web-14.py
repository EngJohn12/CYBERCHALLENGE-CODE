import requests
from bs4 import BeautifulSoup, Comment

url = 'http://web-14.challs.olicyber.it/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))

for comment in comments:
    print(comment)
 
#__________________________________________________________________________________#

# In questo codice, si utilizza la libreria requests per effettuare una richiesta GET 
# all'URL della pagina, quindi si passa il contenuto HTML alla libreria BeautifulSoup 
# per l'analisi. Si utilizza il metodo find_all per cercare tutti gli elementi di tipo 
# Comment nella pagina HTML e si itera su di essi per visualizzarli.


# FLAG ==> flag{50m3b0dy_f0rg07_70_d31373_7hi5}