import re

cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

padrao = re.search(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf)

if padrao:
    print("O CPF está no formato correto.")
else:
    print("Algo deu errado")