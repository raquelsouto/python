cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0 
n = 1
while n <= 5:
    valor = int(input())  
    if valor % 2 == 0:
        cont1 += 1
    if valor % 2 != 0:
        cont2 += 1
    if valor > 0:
        cont3 += 1
    if valor < 0:
        cont4 += 1
    n += 1

print('%d valor(es) par(es)' %cont1)
print('%d valor(es) impar(es)' %cont2)
print('%d valor(es) positivo(s)' %cont3)
print('%d valor(es) negativo(s)' %cont4)