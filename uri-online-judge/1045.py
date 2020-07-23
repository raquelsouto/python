valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
 

if b > a:
    temp = a 
    a = b       
    b = temp

if c > b:
    temp = c
    c = b
    b = temp

if b > a:
    temp = a 
    a = b       
    b = temp

if (a >= b + c):
    print('NAO FORMA TRIANGULO') 

else:
    if (a**2) == ((b**2) + (c**2)):
        print('TRIANGULO RETANGULO')

    if (a**2) > ((b**2) + (c**2)):
        print('TRIANGULO OBTUSANGULO') 

    if (a**2) < ((b**2) + (c**2)):
        print('TRIANGULO ACUTANGULO')

    if (a == b == c):
        print('TRIANGULO EQUILATERO')

    if (a==b!=c) or (a==c!=b) or (b==c!=a):
        print('TRIANGULO ISOSCELES')
