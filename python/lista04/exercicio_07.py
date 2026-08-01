qtd_morango = float(input("Digite a quantidade de morango (kg): "))
qtd_mac = float(input("Digite a quantidade de maçã (kg): "))

if qtd_morango < 5:
    valor_total = qtd_morango * 2.50
else:
    valor_total = qtd_morango * 2.20

if qtd_mac < 5:
    valor_total += qtd_mac * 1.80
else:
    valor_total += qtd_mac * 1.50

print(f"Valor total a ser pago: R$ {valor_total}")
