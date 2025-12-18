frase = input("Digite o texto a ser revisado: ")
substituir = input("Qual palavra deseja substituir? ")
nova_palavra = input("Qual a nova palavra? ")

if substituir in frase:
    frase = frase.replace(substituir, nova_palavra)
    print(frase)
else:
    print("Algo deu errado.")

# Versão com Regex

import re

nova_frase = re.sub(rf'\b{substituir}\b', nova_palavra, frase)
print(nova_frase)