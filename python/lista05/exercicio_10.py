base = int(input("Base: "))
expoente = int(input("Expoente: "))

resultado = 1

for i in range(expoente):
    resultado *= base

print("Resultado:", resultado)