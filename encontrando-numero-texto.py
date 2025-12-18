import re

texto = input("Digite a descrição da receita: ")
padrao = r"\d+"

resultado = re.findall(padrao, texto)[0]

if resultado:
    print(f"O número da receita é: {resultado}")
else:
    print("Algo deu errado")