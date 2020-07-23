valores = input().split()

numero1 = int(valores[0]) 
numero2 = int(valores[1])
numero3 = int(valores[2])

if numero1 < numero2 and numero1 < numero3 and numero2 < numero3:
    print('%d \n%d\n%d' %(numero1, numero2, numero3))
    print('%d \n%d\n%d' %(numero1, numero2, numero3))

elif numero1 < numero3 and numero1 < numero2 and numero3 < numero2:
    print('%d \n%d\n%d' %(numero1, numero3, numero2))
    print('%d \n%d\n%d' %(numero1, numero2, numero3))

elif numero2 < numero3 and numero2 < numero1 and numero3 < numero1:
    print('%d \n%d\n%d' %(numero2, numero3, numero1))
    print('%d \n%d\n%d' %(numero1, numero2, numero3))

elif numero2 < numero1 and numero2 < numero3 and numero1 < numero3:
    print('%d \n%d\n%d' %(numero2, numero1, numero3))
    print('%d \n%d\n%d' %(numero1, numero2, numero3))

elif numero3 < numero1 and numero3 < numero2 and numero2 < numero1:
    print('%d \n%d\n%d' %(numero3, numero2, numero1))
    print('%d \n%d\n%d' %(numero1, numero2, numero3))

elif numero3 < numero1 and numero3 < numero2 and numero1 < numero2:
    print('%d \n%d\n%d' %(numero3, numero1, numero2))
    print('')
    print('%d \n%d\n%d' %(numero1, numero2, numero3))    
    
