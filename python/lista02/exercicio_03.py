# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é positivo, negativo ou zero
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")