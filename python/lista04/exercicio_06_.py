

#Homem velho , Homem jovem, Mulher velha, Mulher jovem,idade h1, idade h2, idade m1, idade m2,produto das
idade_h1 = int(input("Digite a idade do primeiro homem: "))
idade_h2 = int(input("Digite a idade do segundo homem: ")) 
idade_m1 = int(input("Digite a idade da primeira mulher: "))
idade_m2 = int(input("Digite a idade da segunda mulher: "))

if idade_h1 > idade_h2:
    homem_velho = idade_h1
    homem_jovem = idade_h2
else:
    homem_velho = idade_h2
    homem_jovem = idade_h1

if idade_m1 > idade_m2:
    mulher_velha = idade_m1
    mulher_jovem = idade_m2
else:
    mulher_velha = idade_m2
    mulher_jovem = idade_m1

soma = homem_velho + mulher_jovem
produto = homem_jovem * mulher_velha
print(f"Soma(homem mais velho + mulher mais nova): {soma}")
print(f"Produto(homem mais novo * mulher mais velha): {produto}")