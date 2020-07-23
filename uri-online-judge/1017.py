tempo = int(input())
velocidade_media = int(input())
autonomia = 12
distancia_percorrida = tempo * velocidade_media
gasto_combustivel = distancia_percorrida/autonomia
print('%.3f' %(gasto_combustivel))
