n = int(input())

num = n + 1
cont = 0
while cont < 6:
    if num % 2 != 0:
        print('%d' %num)
        cont += 1
    num += 1