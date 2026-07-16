# Entrada de dados (com nomes corretos)
salario_fixo = float(input("Digite o salário fixo por mês: "))
comissao = float(input("Digite o valor da comissão por carro vendido: "))
num_carros_vendidos = int(input("Digite o número de carros vendidos no mês: "))

# Cálculo
salario_total = salario_fixo + (comissao * num_carros_vendidos)

# Saída
print(f"O salário total do vendedor no mês é: R$ {salario_total:.2f}")