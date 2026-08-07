from math import sqrt

# Solicita as coordenadas dos pontos P1 e P2
x1 = float(input("Digite a coordenada x do ponto P1: "))
y1 = float(input("Digite a coordenada y do ponto P1: "))
x2 = float(input("Digite a coordenada x do ponto P2: "))
y2 = float(input("Digite a coordenada y do ponto P2: "))

# Calcula a distância utilizando a fórmula da geometria analítica
distancia = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Exibe o resultado
print(f"A distância entre os pontos P1 e P2 é: {distancia:.2f}")