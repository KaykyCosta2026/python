from datetime import datetime

codigo = input("Código do empregado: ")
ano_nasc = int(input("Ano de nascimento: "))
ano_ingresso = int(input("Ano de ingresso na empresa: "))

ano_atual = datetime.now().year

idade = ano_atual - ano_nasc
tempo = ano_atual - ano_ingresso

if idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >= 25):
    resultado = "Requer aposentadoria"
else:
    resultado = "Não requer"

print(f"Código: {codigo}")
print(f"Idade: {idade}")
print(f"Tempo de trabalho: {tempo}")
print(resultado)