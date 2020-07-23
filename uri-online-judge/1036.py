import math

listas = input().split()
numero_ax2 = float(listas[0])
numero_bx = float(listas[1])
numero_c = float(listas[2])

delta = (numero_bx)**2 - (4*numero_ax2*numero_c)

if delta < 0 or numero_ax2 == 0:
    print('Impossivel calcular')

else:
    if delta == 0:
        raiz_x1 = (-numero_bx)/(2*numero_ax2)
        print('R1 = %.5f' %raiz_x1)
        
    else:
        raiz_y1 = ((-numero_bx) + math.sqrt(delta)) / (2*numero_ax2)
        raiz_y2 = ((-numero_bx) - math.sqrt(delta)) / (2*numero_ax2)
        print('R1 = %.5f' %raiz_y1)
        print('R2 = %.5f' %raiz_y2)
