import requests

url = "http://web-01.challs.olicyber.it/"
response = requests.get(url)

print(response.text)


    # FLAG ==> flag{g3t7ing_4l0ng}