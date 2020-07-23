cont3 = 0
cont2 = 0
cont1 = 0
codigo = 1
while codigo != 4:
    codigo = int(input())
    if codigo == 1:
        cont1 += 1
    elif codigo == 2:
        cont2 += 1
    elif codigo == 3:
        cont3 += 1 

print('MUITO OBRIGADO')
print('Alcool: %d' %(cont1))
print('Gasolina: %d' %(cont2))
print('Diesel: %d' %(cont3))
