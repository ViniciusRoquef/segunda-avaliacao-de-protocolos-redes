#Aqui mostro como utilizar o framework Flask na criação de requisições tipo GET e POST em uma API 
#com formato de arquivo em JSON. Testei tudo usando o POSTMAN e deu certo a inserção e puxar os dados de lá.

from flask import Flask, request 
from database import insertUsuario
import json
app = Flask("Vinicius")

# Método GET
@app.route("/olamundo", methods=["GET"])
def olaMundo(): 
    return {"ola": "mundo"}

# Método POST
@app.route("/cadastra/usuario", methods = ["POST"])
def cadastroUsuario(): 

    body = request.get_json()
    if("nome" not in body ): 
        return {"status": 400, "Mensagem": "O parâmetro de nome cadastro é obrigatório"}
    if("email" not in body): 
        return {"status": 400, "Mensagem": "O parâmetro de email cadastro é obrigatório"}
    if("senha" not in body): 
        return {"status": 400, "Mensagem": "O parâmetro de senha cadastro é obrigatório"}

    usuario = insertUsuario(body["nome"], body["email"], body["senha"])
    return geraResponse(200, "Ususário criado", "user", usuario)

def geraResponse(status, mensagem, nomeConteudo=False, conteudo=False): 
    response = {}
    response["status"] = status 
    response["mensagem"] = mensagem

    if(nomeConteudo and conteudo): 
        response[nomeConteudo]=conteudo 

    return response

app.run()
