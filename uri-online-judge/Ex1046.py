horas = input().split()

hora_inicial = int(horas[0])
hora_final = int(horas[1])

if (0 <= hora_inicial <= 23) and (0 <= hora_final <= 23):
    if hora_inicial == hora_final:
        print('O JOGO DUROU 24 HORA(S)')

    elif hora_inicial > hora_final:
        h_jogo = 24 - hora_inicial
        tempo = h_jogo + hora_final
        print('O JOGO DUROU %d HORA(S)' %tempo)
    else:
        tempo2 = hora_final - hora_inicial
        print('O JOGO DUROU %d HORA(S)' %tempo2)
