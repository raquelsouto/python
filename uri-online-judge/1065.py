contador = 0
n = 1
while n <= 5:
    valor = int(input())
    n += 1
    if valor % 2 == 0:
        contador += 1

print('%d valores pares' %contador)
    