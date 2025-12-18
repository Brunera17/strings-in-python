import re

dados_paciente = input("Digite o nome completo e o ano de nascimento do paciente: ")

conteudo = re.search(r"^([a-zA-Z]+)\s([a-zA-Z]+)\s-\s(\d{4})", dados_paciente)

primeiro_nome = conteudo.group(1)
segundo_nome = conteudo.group(2)
nascimento = conteudo.group(3)

print(f"Primeiro Nome: {primeiro_nome}")
print(f"Sobrenome: {segundo_nome}")
print(f"Ano de Nascimento: {nascimento}")