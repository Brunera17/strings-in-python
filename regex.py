import re

texto = "Entre em contato pelo email support@example.com"

padrao_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

resultado = re.search(padrao_email, texto)
if resultado:
    print("Email encontrado:", resultado.group())
else:
    print("Nenhum email encontrado.")
