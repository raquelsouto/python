soma = 0
cont = cont_ext = 0

n = int(input())
while cont_ext < n:
    v1, v2 = map(int, input().split())
    if v1 % 2 == 0:
        v1 += 1

    while cont < v2:
        if v1 % 2 != 0:
            cont += 1
            soma += v1
        v1 += 1
    print(soma)
    cont_ext += 1
    cont = soma = 0