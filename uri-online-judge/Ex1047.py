tempo = input().split()
hora_inicial = int(tempo[0])
minuto_inicial = int(tempo[1]) 
hora_final = int(tempo[2])
minuto_final = int(tempo[3])

diferenca_hora = (hora_final + 24) - hora_inicial
diferenca_minuto = (minuto_final + 60) - minuto_inicial

if diferenca_hora > 24 and diferenca_minuto > 60:
        diferenca_hora = diferenca_hora - 24
        diferenca_minuto = diferenca_minuto - 60
        print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)' %(diferenca_hora, diferenca_minuto))
        
        if diferenca_hora == 1 and diferenca_minuto <= 59: 
            print('O JOGO DUROU 0 HORA(S) E 60 MINUTO(S)')

    elif diferenca_hora == 24 and diferenca_minuto == 60:
            print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')




