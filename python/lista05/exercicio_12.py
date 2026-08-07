apartamentos = 75
diaria_normal = 292.00

diaria_promocional = diaria_normal * 0.75

ocupacao_normal = apartamentos * 0.50
ocupacao_promocional = apartamentos * 0.80

valor_normal = ocupacao_normal * diaria_normal
valor_promocional = ocupacao_promocional * diaria_promocional

diferenca = valor_promocional - valor_normal

print(f"Diária promocional: R$ {diaria_promocional:.2f}")
print(f"Arrecadação com 80%: R$ {valor_promocional:.2f}")
print(f"Arrecadação com 50%: R$ {valor_normal:.2f}")
print(f"Diferença: R$ {diferenca:.2f}")