maior_nota = -1
vencedora = ""

for i in range(16):
    nome = input("Nome da candidata: ")
    nota = float(input("Nota: "))

    if nota > maior_nota:
        maior_nota = nota
        vencedora = nome

print("\nVencedora:", vencedora)
print("Nota:", maior_nota)