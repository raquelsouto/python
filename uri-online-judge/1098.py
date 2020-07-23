i = 0
j = 1
cont = 0

while i <= 2:
    for num in range(3):
        if i == 0 or i == 1:
            print('I=%d J=%d' %(i, j+i))
        
        elif cont == 10:
            i = 2
            print('I=%d J=%d' %(i, j+i))
        
        else:
            print('I=%.1f J=%.1f' %(i, j+i))
        j += 1
    i += 0.2
    j = 1
    cont += 1
