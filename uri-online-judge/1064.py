cont = 0
n = 1
soma = 0
while n <= 6:
    numero = float(input())
    if numero > 0:
        cont += 1
        if numero > 0:
            soma += numero
            media = (soma)/cont
    n += 1
print('%d valores positivos' %(cont))
print('%.1f' %(media))
