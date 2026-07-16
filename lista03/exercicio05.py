#custo carro novo,custo de fabrica,porcentagem do distribuidor, porcentagem dos inpostos,porcentual do distribuidor 28% inpostos 45%,custo final do consumidor#
custo_fabrica = float(input("Digite o custo de fábrica do carro: "))
porcentagem_distribuidor = 0.28
porcentagem_impostos = 0.45
custo_final = custo_fabrica + (custo_fabrica * porcentagem_distribuidor) + (custo_fabrica * porcentagem_impostos)
print("O custo final do consumidor é: R$", custo_final) 