n1 = int(input())
n2 = int(input())
if n1 < n2:
    temp = n1
    n1 = n2
    n2 = temp
else:
    n1 = n1
    n2 = n2
soma = 0
n2 +=  1
while n2 < n1:
    if n2 % 2 != 0: 
        soma += n2
    n2 += 1
print('%d' %soma)

