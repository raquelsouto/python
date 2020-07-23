tempo = input().split()

hi = int(tempo[0])
mi = int(tempo[1])
hf = int(tempo[2])
mf = int(tempo[3]) 

hi_minuto = hi * 60      #Adicionando os minutos
hf_minuto = hf * 60
hora_final_total_min = hf_minuto + mf
hora_final_total_min = hora_final_total_min + 1440      #Esse valor é 24h em minutos
hora_inicial_total_min = hi_minuto + mi

diferenca = hora_final_total_min - hora_inicial_total_min

if diferenca > 1440:
    diferenca = diferenca - 1440

hora_total = diferenca // 60
minuto_total = diferenca % 60

print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)' %(hora_total, minuto_total))