fim = int(input())
if 0 < fim < 46:
    tn = 0
    t1 = 1

    for i in range(0, fim):
        print(tn, end ='')
        t2 = tn + t1
        tn = t1
        t1 = t2
        if i != fim-1:
            print('', end=' ')
    print('\n',end='')