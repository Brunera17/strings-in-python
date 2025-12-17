mensagem = input("Digite uma mensagem: ")

palavras = []

palavras = mensagem.split()
contador = 1

for palavra in palavras:
    print(f"{contador}. {palavra}")
    contador += 1

