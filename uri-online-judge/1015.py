import math

valor_x1, valor_y1 = map(float, input().split())
valor_x2, valor_y2 = map(float, input().split())

pontos = (valor_x2 - valor_x1)**2 + (valor_y1 - valor_y2)**2
distancia = math.sqrt(pontos)
print('%.4f' %(distancia))
