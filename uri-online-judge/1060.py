cont = 0
n = 1
while n <= 6:
    num = float(input())
    if num > 0:
        cont += 1
    n += 1
    
print('%d valores positivos' %(cont))