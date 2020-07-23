n1 = 1
n2 = 0
while n1 != n2:
    n1, n2 = map(int, input().split())
    if n1 > n2:
        print('Decrescente')
    elif n2 > n1:
        print('Crescente')
