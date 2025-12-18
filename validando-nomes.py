import re

nome = input("Digite o nome do cliente para validação: ")

letra_maiuscula = re.match(r'[A-Z]{1}', nome)
contem_numeros = re.findall(r'\d+', nome)

if letra_maiuscula and not contem_numeros:
    print("Nome válido")
else:
    print("Nome inválido")