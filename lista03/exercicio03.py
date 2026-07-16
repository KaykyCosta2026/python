#idade pessoa em  expressa anos messes dias)escreva a idadedessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.##)
anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite a idade em meses: ")) 
dias = int(input("Digite a idade em dias: "))
idade_em_dias = (anos * 365) + (meses * 30) + dias
print("A idade da pessoa expressa em dias é: ", idade_em_dias)
