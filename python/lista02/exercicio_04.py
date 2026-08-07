# Solicita o salário atual e o valor do aumento
salario_atual = float(input("Digite o salário atual do funcionário (R$): "))
aumento = float(input("Digite o valor do aumento (R$): "))

# Calcule o novo salário
novo_salario = salario_atual + aumento

# Imprime o resultado formatado
print(f"O novo salário do funcionário é: R$ {novo_salario:.2f}")