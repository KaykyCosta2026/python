#numero  conta cliente#c, saldo debito credito#]
numero_conta = int(input("Digite o número da conta: "))
saldo = float(input("Digite o saldo atual da conta: "))
debito = float(input("Digite o valor do débito: "))
credito = float(input("Digite o valor do crédito: "))
saldo_atual = saldo - debito + credito
print(f"O saldo atual da conta é: R$ {saldo_atual:.2f}")
if saldo_atual >= 0:
    print("Saldo positivo.")
else:
    print("Saldo negativo.")
    