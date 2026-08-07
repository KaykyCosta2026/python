soma = 0

for num in range(2, 101):
    primo = True

    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        soma += num

print("Soma dos números primos:", soma)