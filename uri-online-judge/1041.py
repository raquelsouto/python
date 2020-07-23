valores = input().split()
valor_x = float(valores[0])
valor_y = float(valores[1])

if valor_x == 0 and valor_y == 0:
    print('Origem')

elif valor_x != 0 and valor_y == 0:
    print('Eixo X')
    
elif valor_x == 0 and valor_y != 0:
    print('Eixo Y')

elif valor_x > 0 and valor_y > 0:
    print('Q1')

elif valor_x < 0 and valor_y > 0:
    print('Q2')

elif valor_x < 0 and valor_y < 0:
    print('Q3')

else:
    print('Q4')
