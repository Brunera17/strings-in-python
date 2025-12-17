url = input("Digite a URL para verificação: ")

if url.startswith("https://") and url.endswith(".com"):
    print("URL válida!")
else:
    print("URL inválida!")