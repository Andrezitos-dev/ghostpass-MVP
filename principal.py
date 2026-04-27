# Secção de Funções 

import secrets
import string 

inbox = {} # dicionário para armazenar as caixas de entrada dos emails

def gerar_senha(tamanho):
    carcteres = string.ascii_letters + string.digits + string.punctuation
    senha = ""
    for i in range(tamanho):
        senha += secrets.choice(carcteres)
    return senha

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

# Teste de Função 
print(f"Gerar email: {gerar_email()}")
print(f"Gerar senha: {gerar_senha(16)}")
email = criar_email()
print(f"Ver a caixa de entrada: {ver_inbox(email)}")
receber_email(email, "Teste", "Este é um email de teste.")
print(f"Ver a caixa de entrada após receber um email: {ver_inbox(email)}")



