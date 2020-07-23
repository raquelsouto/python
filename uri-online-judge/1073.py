n = int(input())
cont = 2
if 5 < n < 2000:
    while cont <= n:
        if n % 2 == 0:
            multi = cont ** 2
            print('%d^2 = %d' %(cont, multi))
        cont += 2