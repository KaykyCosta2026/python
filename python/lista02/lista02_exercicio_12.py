#valor pago,valor pago pelo cliente, troco 
valor_produto = float(input("Digite o valor do produto: "))
valor_pago = float(input("Digite o valor pago pelo cliente: "))
if valor_pago < valor_produto:
    print("O valor pago é insuficiente para cobrir o valor do produto.")
else:
    troco = valor_pago - valor_produto
    print("O troco é: ", troco)