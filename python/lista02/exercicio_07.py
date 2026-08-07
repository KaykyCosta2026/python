#IMC mensagem indicando se a pessoa está abaixo do peso, no peso ideal ou acima do peso, de acordo com o IMC (Índice de Massa Corporal). O IMC é calculado dividindo o peso (em kg) pela altura (em metros) ao quadrado. A classificação do IMC é a seguinte: abaixo de 18,5: abaixo do peso; entre 18,5 e 24,9: peso ideal; entre 25 e 29,9: acima do peso; 30 ou mais: obesidade.##
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está no peso ideal.")
elif 25 <= imc < 30:
    print("Você está acima do peso.")
else:
    print("Você está obeso.")