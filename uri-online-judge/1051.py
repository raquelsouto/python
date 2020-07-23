salario = float(input())

if salario > 0 and salario <= 2000:
   print('Isento')

elif salario >= 2000.01 and salario <= 3000:
    valor1 = salario - 2000
    imposto1 = (valor1 * 0.08)
    print('R$ %.2f' %imposto1)

elif salario > 3000.01 and salario <= 4500:
    valor2 = salario - 2000
    taxa2 = valor2 - 1000
    imposto2 = (1000 * 0.08) + (taxa2 * 0.18)
    print('R$ %.2f' %imposto2)

else:
    valor3 = salario - 2000
    taxa3 = valor3 - 1000
    excedente3 = taxa3 - 1500
    imposto3 = (1000 * 0.08) + (1500 * 0.18) + (excedente3 * 0.28)
    print('R$ %.2f' %imposto3)
    

    