num = int(input())
if num % 2 == 0:
    n = 12
else: 
    n = 11

cont = 1
while cont <= n:
    if num % 2 != 0:
        print('%d' %num)
    num += 1
    cont += 1
    
    
