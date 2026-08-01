#jornada de trabalho#
jornada_trabalho = int(input("Digite a jornada de trabalho em horas: "))
if jornada_trabalho > 40:
    horas_extras = jornada_trabalho - 40
    print(f"Você trabalhou {horas_extras} horas extras.")
else:
    print("Você não trabalhou horas extras.")