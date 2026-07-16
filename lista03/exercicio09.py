#hora inicio,hora fim#
hora_inicio = int(input("Digite a hora de início do jogo (0-23): "))
hora_fim = int(input("Digite a hora de término do jogo (0-23): "))
if hora_fim > hora_inicio:
    duracao = hora_fim - hora_inicio
    print(f"A duração do jogo é de {duracao} horas.")
else:
    print("A hora de término deve ser posterior à hora de início.")