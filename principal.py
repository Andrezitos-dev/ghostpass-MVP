import secrets
import string 

# Definir o que pode ter na sua senha
caracteres =string.ascii_letters + string.digits * 5 + string.punctuation
# gerar uma senha aleatória 
senha = ''.join(secrets.choice(caracteres)) 

for i in range (0, 15):
    senha += secrets.choice(caracteres)

print(f"Sua senha gerada aleatoriamente é: {senha}")

# Email descartável

email = "Exemplo123@gmail.com"
