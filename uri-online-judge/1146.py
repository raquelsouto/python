num = 1
while num != 0:
    num = int(input())
    if num <= 0:
        break
    for i in range(1, num+1):
        if i != num:
            print(i, end=' ')
        else:
            print(i, end='\n')