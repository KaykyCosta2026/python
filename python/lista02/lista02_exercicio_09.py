#determinação idade #
idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 2:
    print("Sua classificação faixa etária é: bebe")

elif idade >= 3 and idade <= 12:   
    print("Sua classificação faixa etária é: criança")
elif idade >= 13 and idade <= 17:
    print("Sua classificação faixa etária é: adolescente")
elif idade >= 18 and idade <= 64:
    print("Sua classificação faixa etária é: adulto")
elif idade >= 65:
    print("Sua classificação faixa etária é: idoso")