valor = int(input())
valor_temp = valor

notas100 = valor//100
valor = valor - (notas100*100)

notas50 = valor//50
valor = valor - (notas50*50)

notas20 = valor//20
valor = valor - (notas20*20)

notas10 = valor//10
valor = valor - (notas10*10)

notas5 = valor//5
valor = valor - (notas5*5)

notas2 = valor//2
valor = valor - (notas2*2)

notas1 = valor//1
valor = valor - (notas1*1)

print('%d' %valor_temp)
print('%d nota(s) de R$ 100,00' %(notas100))
print('%d nota(s) de R$ 50,00' %(notas50))
print('%d nota(s) de R$ 20,00' %(notas20))
print('%d nota(s) de R$ 10,00' %(notas10))
print('%d nota(s) de R$ 5,00' %(notas5))
print('%d nota(s) de R$ 2,00' %(notas2))
print('%d nota(s) de R$ 1,00' %(notas1))




