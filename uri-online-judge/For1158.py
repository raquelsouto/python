n = int(input())

for i in range(n):
    inicio, v2 = map(int, input().split())
    if inicio % 2 == 0:
        inicio += 1

    soma = 0
    v2 = inicio + (v2-1)*2
    for i in range(inicio, v2+1, 2):
        soma += i
    print(soma)