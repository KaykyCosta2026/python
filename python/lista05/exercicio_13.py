# Valores fixos
preco_chopp = 5.00
preco_pizza = 50.00
preco_cobertura = 2.50

# Entrada de dados
quantidade_chopp = int(input("Quantidade de chopps: "))
quantidade_coberturas = int(input("Quantidade de coberturas da pizza: "))
pessoas = int(input("Quantidade de pessoas na mesa: "))

# Cálculos
valor_chopp = quantidade_chopp * preco_chopp
valor_pizza = preco_pizza + (quantidade_coberturas * preco_cobertura)

total = valor_chopp + valor_pizza

# Acrescenta 10% do garçom
total_com_garcom = total * 1.10

# Valor por pessoa
valor_por_pessoa = total_com_garcom / pessoas

# Saída
print(f"\nValor dos chopps: R$ {valor_chopp:.2f}")
print(f"Valor da pizza: R$ {valor_pizza:.2f}")
print(f"Total sem 10%: R$ {total:.2f}")
print(f"Total com 10% do garçom: R$ {total_com_garcom:.2f}")
print(f"Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}")