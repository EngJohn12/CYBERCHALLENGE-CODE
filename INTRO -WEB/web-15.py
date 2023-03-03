import requests
from bs4 import BeautifulSoup

url = 'http://web-15.challs.olicyber.it/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
resources = set()

# Estrae i link ai fogli di stile
for link in soup.find_all('link'):
    if link.has_attr('href') and link.has_attr('rel') and 'stylesheet' in link['rel']:
        resources.add(link['href'])

# Estrae i link ai file javascript
for script in soup.find_all('script'):
    if script.has_attr('src'):
        resources.add(script['src'])

# Scarica ogni risorsa e cerca la flag all'interno
for resource in resources:
    response = requests.get(resource)
    if response.status_code == 200:
        content = response.text
        if 'flag{' in content:
            print('Flag trovata in {}:'.format(resource))
            print(content)
