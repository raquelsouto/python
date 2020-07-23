n1 = n2 = cont = 0 

numero = int(input())
while cont < numero: 
    n1, n2 = map(int, input().split())
    
    if n1 == 0 and n2 == 0 or n2 != 0:
        div = n1 / n2 
        print('%.1f' %div)
    elif n1 != 0 and n2 == 0:
        print('divisao impossivel')
    elif n1 != 0 and n2 != 0:
        div = n1/n2
        print('%.1f' %div)
    cont += 1
