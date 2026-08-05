#tres numeros determinação de um lados de um triangulo,equilatero,isoceles,escaleno,
lado1 = int(input("Digite o valor do primeiro lado: "))
lado2 = int(input("Digite o valor do segundo lado: "))
lado3 = int(input("Digite o valor do terceiro lado: "))
if lado1 == lado2 and lado2 == lado3:
    print("O triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é isósceles.")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("O triângulo é escaleno.") 
else:
    print("Os valores fornecidos não formam um triângulo.")