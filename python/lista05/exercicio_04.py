primeiro = float(input("Digite o primeiro valor: "))
segundo = float(input("Digite o segundo valor: "))

while segundo == 0:
    print("O segundo valor não pode ser zero!")
    segundo = float(input("Digite outro valor: "))

resultado = primeiro / segundo

print("Resultado da divisão:", resultado)