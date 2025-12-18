titulo = input("Digite o título do livro: ")
letra_inicial = input("Digite a letra inicial para pesquisa: ")
palavras = []
palavras = titulo.split()

for palavra in palavras:
    if palavra.startswith(letra_inicial):
        print(palavra)


# Exemplo com Regex
import re

palavras = re.findall(rf'\b{letra_inicial}[a-zà-ÿ]*', titulo, re.IGNORECASE)
print(palavras)