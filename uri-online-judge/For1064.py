n = soma = cont = 0

while n < 6:
    num = float(input())
    if num > 0: 
        cont += 1
        soma += num
        media = soma/cont
    n += 1

print('%d valores positivos' %cont)
print('%.1f' %media)