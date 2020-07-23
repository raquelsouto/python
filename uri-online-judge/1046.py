valor = input().split()

hora_inicial = int(valor[0])
hora_final = int(valor[1])

if (0 <= hora_inicial <= 23) and (0 <= hora_final <= 23):
    diferenca = (hora_final + 24) - hora_inicial
    if diferenca > 24:
        diferenca -= 24
    
    print('O JOGO DUROU %d HORA(S)' %diferenca)