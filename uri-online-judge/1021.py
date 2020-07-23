valor = float(input())
valor += 0.001

notas100 = valor//100
valor = valor - (notas100*100)
notas50 = valor // 50
valor = valor - (notas50*50)
notas20 = valor // 20
valor = valor - (notas20*20)
notas10 = valor // 10
valor = valor - (notas10*10)
notas5 = valor // 5
valor = valor - (notas5*5)
notas2 = valor // 2
valor = valor - (notas2*2)

moedas1 = valor // 1
valor = valor - (moedas1*1)
moedas50 = valor // 0.50
valor = valor - (moedas50 * 0.50)
moedas25 = valor // 0.25
valor = valor - (moedas25*0.25)
moedas10 = valor // 0.10
valor = valor - (moedas10 * 0.10)
moedas5 = valor // 0.05
valor = valor - (moedas5 * 0.05)
moedas001 = valor // 0.01
valor = valor - (moedas001 * 0.01)

print('NOTAS:')
print('%d nota(s) de R$ 100.00' %notas100)
print('%d nota(s) de R$ 50.00' %notas50)
print('%d nota(s) de R$ 20.00' %notas20)
print('%d nota(s) de R$ 10.00' %notas10)
print('%d nota(s) de R$ 5.00' %notas5)
print('%d nota(s) de R$ 2.00' %notas2)
print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' %moedas1)
print('%d moeda(s) de R$ 0.50' %moedas50)
print('%d moeda(s) de R$ 0.25' %moedas25)
print('%d moeda(s) de R$ 0.10' %moedas10)
print('%d moeda(s) de R$ 0.05' %moedas5)
print('%d moeda(s) de R$ 0.01' %moedas001)
