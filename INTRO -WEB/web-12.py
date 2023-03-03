import requests
from bs4 import BeautifulSoup

# URL della pagina web
url = 'http://web-12.challs.olicyber.it/'

# Scarica la pagina web
response = requests.get(url)

# Parsa la pagina web con BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Trova tutti i tag 'p' nella pagina web
paragraphs = soup.find_all('p')

# Estrai il testo del secondo paragrafo
second_paragraph = paragraphs[1].text.strip()

# Stampa la flag
print(second_paragraph)

# FLAG ==> flag{7h3_14ngu4g3_0f_7h3_w3b}

