n = int(input())
contador = 0
cont_i = 0
cont_j = 0
while contador < n:
    num = int(input())
    if 10 <= num <= 20:
        cont_i += 1
    else:
        cont_j += 1
    contador += 1
print('%d in' %cont_i)
print('%d out' %cont_j)
