numero = int(input("Digite um número: "))

divisores = []

for i in range(2, numero):
    if numero % i == 0:
        divisores.append(i)

if len(divisores) == 0 and numero > 1:
    print("É primo.")
else:
    print("Não é primo.")
    print("Divisível por:", divisores)