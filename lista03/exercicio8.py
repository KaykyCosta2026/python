#maçãs 
numero_macas = int(input("Digite o número de maçãs que deseja comprar: "))
if numero_macas < 12:
    preco_unitario = 1.30
else:
    preco_unitario = 1.00
preco_total = numero_macas * preco_unitario
print(f"O preço total da compra é: R$ {preco_total:.2f}")