from math import sqrt
X1= float(input("Digite o valor de X1: "))
Y1= float(input("Digite o valor de Y1: "))
X2= float(input("Digite o valor de X2: "))
Y2= float(input("Digite o valor de Y2: "))
distancia = sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
print(f"A distância entre os pontos é: {distancia:.2f}")