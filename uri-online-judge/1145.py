valor = input().split()
v1 = int(valor[0])
v2 = int(valor[1])
    
if 1 < v1 < 20 and v2 > v1:
    for i in range(1, v2+1):
        if i == v2:
            print(i, end='\n')
        else:
            if i % (v1) != 0:
                print(i, end=' ')
            else:
                print(i, end='\n')