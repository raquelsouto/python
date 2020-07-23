n = 0
media = cont = 0
while n >= 0:
    n = float(input())
    if n > 0:
        media += n
        cont += 1

soma = media/cont
print('%.2f' %soma)