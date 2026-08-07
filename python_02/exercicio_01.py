preco = int(input("Digite o preço da mercadoria: "))
quantidade = int(input("Digite o percentual do desconto: "))

desconto = preco * (quantidade / 100)
precoapagar = preco - desconto
print(f"O desconto é de R$ {desconto:.2f}")
print(f"O preço a pagar é de R$ {precoapagar:.2f}")
