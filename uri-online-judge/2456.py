lista = list(map(int, input().split()))

for i in range (0, len(lista)):
    if lista == sorted(lista):
        print('C')
    
    elif lista == sorted(lista, reverse=True):
        print('D')
    
    else:
        print('N')
