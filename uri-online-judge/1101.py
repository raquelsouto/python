v1 = v2 = 1
while v1 > 0 and v2 > 0:
    valor = input().split()
    v1 = int(valor[0])
    v2 = int(valor[1])
    
    if v1 > 0 and v2 > 0:
        if v1 > v2:
            v1, v2 = v2, v1

        soma = 0
        for i in range(v1, v2+1):
            soma += i
            print('%d' %i, end=' ')
        print('Sum=%d' %soma)
