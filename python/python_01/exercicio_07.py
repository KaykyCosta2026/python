nome = input("Digite o nome do seu corretor: ")
salario = float(input("Digite o valor do salário do corretor: "))
imovel = float(input("Digite o valor do imóvel: "))
vallortotalvendas = float(input("Digite o valor total das vendas do corretor: "))
comissao = imovel * 0.05
salarioTotal = salario + comissao
print(f"O salário total do corretor {nome} é: R$ {salarioTotal:.2f}")
