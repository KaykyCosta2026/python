# Programa que verifica se um número é positivo, negativo ou zero

# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Verifica e imprime a mensagem correspondente
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
