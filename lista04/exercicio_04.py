#nome de 2 times,numero de gols marcados pelo time 1 e pelo time 2. Mostrar o nome do vencedor ou se houve empate.
time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")
gols_time1 = int(input(f"Digite o número de gols marcados pelo {time1}: "))
gols_time2 = int(input(f"Digite o número de gols marcados pelo {time2}: "))
if gols_time1 > gols_time2:
    print(f"O vencedor é o {time1}!")
elif gols_time2 > gols_time1:
    print(f"O vencedor é o {time2}!")
else:
    print("O jogo terminou empatado!")