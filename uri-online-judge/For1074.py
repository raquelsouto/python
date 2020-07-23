n = int(input())

cont_ratos = cont_coelhos = cont_sapos = 0
soma = 0
for teste in range(1, n+1):
    cobaias = input().split()
    c1 = int(cobaias[0])
    c2 = cobaias[1].upper()
    soma += c1

    if c2 == 'C':
        cont_coelhos += c1
    
    elif c2 == 'R':
        cont_ratos += c1
    
    elif c2 == 'S':
        cont_sapos += c1

print('Total: %d cobaias' %soma)
print('Total de coelhos: %d' %cont_coelhos)
print('Total de ratos: %d' %cont_ratos)
print('Total de sapos: %d' %cont_sapos)

porc_coelhos = ((cont_coelhos*100)/soma)
porc_ratos = ((cont_ratos*100)/soma)
porc_sapos = ((cont_sapos*100)/soma)

print('Percentual de coelhos: %.2f %%' %porc_coelhos)
print('Percentual de ratos: %.2f %%' %porc_ratos)
print('Percentual de sapos: %.2f %%' %porc_sapos)