import requests, re
from bs4 import BeautifulSoup,Comment

url="http://0.0.0.0:8000/victima.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
correos= soup.find_all(string=re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'))
print("---Correos encontrados--")
for correo in correos:
    print(correo)
print("---Comentarios encontrados---")
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for comment in comments:
    print(comment)



