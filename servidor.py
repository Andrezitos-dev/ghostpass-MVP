# Secção de Funções 

import random 
import secrets
import string 
import math

inbox = {} # dicionário para armazenar as caixas de entrada dos emails

def gerar_senha(tamanho=16):

    # Definir os caracteres
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = "!#@$%&*?"

    # Definir quantidades
    qtd_letras = math.ceil(tamanho * 0.5)
    qtd_numeros = math.ceil(tamanho * 0.25)
    qtd_simbolos = tamanho - qtd_letras - qtd_numeros

    senha = []

    # Adicionar letras
    for _ in range(qtd_letras):
        senha.append(secrets.choice(letras))

    # Adicionar números
    for _ in range(qtd_numeros):
        senha.append(secrets.choice(numeros))

    # Adicionar simbolos
    for _ in range(qtd_simbolos):
        senha.append(secrets.choice(simbolos))

    # Embaralhar 
    random.shuffle(senha)

    return "".join(senha)

def gerar_email():
    caracteres = string.ascii_letters + string.digits
    nome = ""
    for i in range(10):
        nome += secrets.choice(caracteres)
    return nome + "@ghostpass.com"

def criar_email():
    email = gerar_email()
    inbox[email] = [] # cria uma caixa de entrada vazia
    return email

def ver_inbox(email):
    return inbox.get(email, [])

def receber_email(email, assunto, conteudo):
    if email in inbox:
        inbox[email].append({"assunto": assunto, "conteudo": conteudo})

# Secção do API
from flask import Flask, jsonify, request
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route("/api/identidade", methods=["GET"])
def identidade():
    novo_email = criar_email()
    nova_senha = gerar_senha(16)

    return jsonify({
        "email": novo_email,
        "senha": nova_senha
    })

#🔹criar email 
@app.route("/api/email/", methods=["GET"] )
def email():
    novo_email = criar_email()
    return jsonify({"email": novo_email})

#🔹 ver inbox 
@app.route("/api/inbox/<email>", methods=["GET"])
def receber():
    data = request.json
    receber_email(data["email"],
                  data["assunto"],
                  data["conteudo"])
    return jsonify({"msg": "Email recebido"})

if __name__ == "__main__":
    app.run(debug=True)
