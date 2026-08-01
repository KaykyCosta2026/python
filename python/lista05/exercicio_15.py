
#teste de envio#
import random 
acima_de_5 = 0
divisiveis_por_3 = 0
numeros = []

for i in range(20):
    numero = random.randint(0, 10)
    numeros.append(numero)

    if numero > 5:
        acima_de_5 += 1

    if numero % 3 == 0:
        divisiveis_por_3 += 1

print("Números sorteados:")
print(numeros)

print("Quantidade de números acima de 5:", acima_de_5)
print("Quantidade de números divisíveis por 3:", divisiveis_por_3)