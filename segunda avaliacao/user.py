import json
from unicodedata import name
from urllib import request
import requests


# Método Get -> Traz informações no arquivo JSON
request = requests.get('https://jsonplaceholder.typicode.com/users') 
users = json.loads(request.content); 

for user in users: 
    print('Olá: ' + user['name'])


# Método POST -> Adiciona argumentos ao arquivo JSON
informacoes = '''{
    "name": "Allan Roque", 
    "username": "allanrocksti", 
    "email": "allan@teste.com",
    "senha": "mudar123"
    }'''
request = requests.post('https://jsonplaceholder.typicode.com/users', data=informacoes)
users = json.loads(request.content); 
print(request.json())

# Método PATCH -> Atualiza informações do arquivo JSON
informacoes = '''{
    "name": "Allan Roque", 
    "username": "viniciusroqf", 
    "email": "vinicius@teste.com"
    "senha": "mudar123
    }'''
request = requests.patch('https://jsonplaceholder.typicode.com/users', data=informacoes)
users = json.loads(request.content); 
print(request.json())

# Método DELETE -> Deleta informações do arquivo JSON
request = requests.patch('https://jsonplaceholder.typicode.com/users')