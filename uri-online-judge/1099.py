num = int(input())

cont_ext = cont = 0
while cont_ext < num: 
    lista = []
    n1, n2 = map(int, input().split())

    if n2 < n1: 
        n1, n2 = n2, n1

    cont = n1 + 1

    while cont < n2:
        if cont % 2 != 0:
            lista.append(cont)
        cont += 1
    
    cont_ext += 1
    soma = sum(lista)
    print('%d' %soma)

