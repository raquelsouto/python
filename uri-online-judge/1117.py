media = 0
cont = 1
cont_n = 
while cont_n <= 2:
    nota = float(input())
    if 0 <= nota <= 10:
        media += nota
        cont_n += 1
    else:
        print('nota invalida')
    cont += 1
media = media/2
print('media = %.2f' %media)