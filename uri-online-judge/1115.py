n1 = 1
n2 = 1
while n1 != 0 or n2 != 0:    
    n1, n2 = map(int, input().split())
    if n1 > 0 and n2 > 0:
        print('primeiro')
    elif n1 < 0 and n2 > 0:
        print('segundo')
    elif n1 < 0 and n2 < 0:
        print('terceiro')
    elif n1 > 0 and n2 < 0:
        print('quarto')
    elif n1 == 0 or n2 == 0:
        break