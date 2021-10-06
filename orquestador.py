import requests 
from decouple import config
import json as js
URL = config('LOCALHOST',cast=str)

#print(URL)

response = requests.get(URL)
print(URL)

i = 0
valor = 0
while i < 50:
    response = requests.post(URL+"/suma", json={"variable": valor})
    valor = response.json().get('variable')
    print(valor)
    i= i+1
#En el orquestador tendre que crear una función que me reciba el tamaño de la ram de los otros servicios 
#y de ahí definir con cual se va empezar 