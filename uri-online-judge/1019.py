tempo = int(input())
horas = tempo // 3600
minutos = tempo % 3600
minutos_final = minutos // 60
segundos = minutos % 60

print('%d:%d:%d' %(horas,minutos_final,segundos))

