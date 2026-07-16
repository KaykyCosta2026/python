#quantidade máxima em estoque, quantidade mínima em estoque, quantidade atual em estoque
quantidade_maxima = int(input("Digite a quantidade máxima em estoque: "))
quantidade_minima = int(input("Digite a quantidade mínima em estoque: "))
quantidade_atual = int(input("Digite a quantidade atual em estoque: "))

#calcular a média
media = (quantidade_maxima + quantidade_minima) / 2

#verificar se é necessário fazer pedido
if quantidade_atual < media:
    print("É necessário fazer pedido.")
else:
    print("Não é necessário fazer pedido.")