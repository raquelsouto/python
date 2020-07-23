n = int(input())
valor = 0
cont = 0
lista_numeros = []
while valor < n:         
    num = int(input())     
    lista_numeros.append(num)
    valor += 1

while cont < n:
    num = lista_numeros[cont]
    if num % 2 == 0 and num != 0:
        print('EVEN ',end='')
    if num % 2 != 0:
        print('ODD ',end='')
    if num > 0:
        print('POSITIVE')
    if num < 0: 
        print('NEGATIVE')
    if num == 0:
        print('NULL')
    cont += 1 