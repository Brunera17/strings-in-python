frase = input("Digite o texto a ser revisado: ")
substituir = input("Qual palavra deseja substituir? ")
novaPalavra = input("Qual a nova palavra? ")

if substituir in frase:
    frase = frase.replace(substituir, novaPalavra)
    print(frase)
else:
    print("Algo deu errado.")