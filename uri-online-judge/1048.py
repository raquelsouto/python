salario = float(input())

if salario == 0 or salario <= 400:
    salario_novo = salario + (salario*0.15)
    reajuste = salario * 0.15
    print('Novo salario: %.2f' %salario_novo)
    print('Reajuste ganho: %.2f' %reajuste)
    print('Em percentual: 15 %')

elif salario >= 400.001 and salario <= 800:
    salario_novo = salario + (salario*0.12)
    reajuste = salario * 0.12
    print('Novo salario: %.2f' %salario_novo)
    print('Reajuste ganho: %.2f' %reajuste)
    print('Em percentual: 12 %')

elif salario >= 800.001 and salario <= 1200:
    salario_novo = salario + (salario*0.10)
    reajuste = salario * 0.10
    print('Novo salario: %.2f' %salario_novo)
    print('Reajuste ganho: %.2f' %reajuste)
    print('Em percentual: 10 %')

elif salario >= 1200.001 and salario <= 2000:
    salario_novo = salario + (salario*0.07)
    reajuste = salario * 0.07
    print('Novo salario: %.2f' %salario_novo)
    print('Reajuste ganho: %.2f' %reajuste)
    print('Em percentual: 7 %')

else:
    salario_novo = salario + (salario*0.04)
    reajuste = salario * 0.04
    print('Novo salario: %.2f' %salario_novo)
    print('Reajuste ganho: %.2f' %reajuste)
    print('Em percentual: 4 %')