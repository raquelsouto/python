lista = input().split()
primeiro = int(lista[0])
segundo = int(lista[1])
terceiro = int(lista[2])
quarto = int(lista[3])

if segundo > terceiro and quarto > primeiro and (terceiro + quarto) > (primeiro + segundo) and terceiro >= 0 and quarto >= 0 and primeiro % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')

