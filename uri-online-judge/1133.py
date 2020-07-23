n1 = int(input())
n2 = int(input())
if n2 > n1:
    temp = n1
    n1 = n2
    n2 = temp
else:
    n1 = n1
    n2 = n2
 
cont = n2 + 1 
while cont < n1:
    if cont % 5 == 2 or cont % 5 == 3:
        print('%d' %cont)
    cont += 1
