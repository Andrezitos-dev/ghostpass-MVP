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

def gerar_nome_email():
    palavras_1 = ["Galáxia", "Universo", "Estrela", "Planeta", "Asteroide", "Cometa", "Supernova", "Nebulosa", "Órbita","Espaço","Cosmos", "Dimensão", "Multiverso", "Nave", "Foguete", "Cruzeiro", "Cargueiro", "Sonda","Satélite", "Estação","Base", "Colônia", "Império", "República", "Federação", "Aliança", "Rebelião","Ciborgue", "Androide", "Robô","Inteligência", "Holograma", "Matriz", "Rede", "Sistema", "Servidor", "Código", "Algoritmo", "Vírus", "Programa","Chip", "Processador", "Circuito", "Bateria", "Reator", "Plasma", "Laser", "Fóton", "Íon", "Quantum","Átomo", "Molécula", "Genoma", "Clone", "Mutante", "Alienígena", "Extraterrestre", "Invasor", "Espécie", "Raça","Portal", "Fenda", "Anomalia", "Paradoxo", "Cronos", "Tempo", "Futuro", "Hiperespaço", "Dobra", "Velocidade","Gravidade", "Antimatéria", "Energia", "Escudo", "Campo", "Força", "Armadura", "Exotraje", "Mecha", "Drone","Hoverboard", "Speeder", "Blaster", "Canhão", "Torpedo", "Míssil", "Ogiva", "Bomba", "Detonador", "Radar","Scanner", "Sensor", "Transmissor", "Comunicador", "Frequência", "Sinal", "Rádio", "Ótica", "Lente", "Visor","Tela", "Painel", "Console", "Computador", "Máquina", "Engenho", "Aparelho", "Dispositivo", "Gadget", "Módulo","Cápsula", "Incubadora", "Câmara", "Cilindro", "Tubo", "Laboratório", "Pesquisa", "Ciência","Experimento", "Descoberta","Invenção", "Tecnologia", "Ciberespaço", "Sinergia", "Vácuo"]
    palavras_2 = ["Épico", "Mágico", "Místico", "Feérico", "Sombrio", "Amaldiçoado", "Abençoado", "Sagrado", "Profano","Divino", "Celestial", "Heróico", "Lendário", "Mítico", "Ancestral", "Antigo", "Esquecido", "Perdido","Oculto", "Secreto", "Misterioso", "Enigmático", "Arcano", "Esotérico", "Alquímico", "Encantado","Enfeitiçado", "Assombrado","Macabro", "Gótico", "Real", "Nobre", "Plebeu", "Feudal", "Imperial", "Soberano", "Majestoso", "Imponente","Grandioso", "Rústico", "Bárbaro", "Selvagem", "Primitivo", "Tribal", "Pagão", "Herege", "Ortodoxo", "Zeloso","Devoto", "Piedoso", "Cruel", "Sanguinário", "Impiedoso", "Tirânico", "Justo", "Valente", "Corajoso", "Destemido","Honrado", "Leal", "Traiçoeiro", "Desleal", "Falso", "Enganoso", "Ilusório", "Fantástico", "Quimérico","Dracônico","Élfico", "Anão", "Órquico", "Goblinoide", "Titânico", "Colossal", "Gigante", "Minúsculo", "Etéreo", "Espectral","Fantasmagórico", "Espiritual", "Elemental", "Flamejante", "Gélido", "Congelado", "Rochoso", "Terroso","Ventoso", "Tempestuoso","Abissal", "Profundo", "Subterrâneo", "Cavernoso", "Montanhoso", "Florestal", "Silvestre", "Luminoso", "Brilhante", "Ofuscante","Tenebroso", "Escuro", "Noturno", "Crepuscular", "Diurno", "Dourado", "Prateado", "Férreo", "Acobreado", "Enferrujado","Polido", "Afiado", "Cego", "Quebrado", "Forjado", "Temperado", "Rúnico", "Protetor", "Defensivo", "Ofensivo","Destrutivo", "Restaurador", "Curativo", "Venenoso", "Letal"]

    nome = secrets.choice(palavras_1) + secrets.choice(palavras_2)
    numero = secrets.randbelow(999)

    return f"{nome}.{numero}" + "@ghostpass.com"

def criar_email():
    email = gerar_nome_email()
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

# GERAR IDENTIDADE
@app.route("/api/identidade", methods=["GET"])
def identidade():

    novo_email = criar_email()
    nova_senha = gerar_senha(16)

    return jsonify({
        "email": novo_email,
        "senha": nova_senha
    })


# VER INBOX
@app.route("/api/inbox/<email>", methods=["GET"])
def inbox_view(email):

    return jsonify(ver_inbox(email))


# RECEBER EMAIL
@app.route("/api/receber", methods=["POST"])
def receber():

    data = request.json

    receber_email(
        data["email"],
        data["assunto"],
        data["conteudo"]
    )

    return jsonify({
        "msg": "Email recebido"
    })


# GERAR EMAIL
@app.route("/api/email", methods=["GET"])
def email():

    novo_email = criar_email()

    return jsonify({
        "email": novo_email
    })


if __name__ == "__main__":
    app.run(debug=True)
