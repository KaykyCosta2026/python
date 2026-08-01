n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media_ex = float(input("Média dos exercícios: "))

media = (n1 + n2 * 2 + n3 * 3 + media_ex) / 7

if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
else:
    conceito = "D"

print(f"Média: {media:.2f}")
print("Conceito:", conceito)