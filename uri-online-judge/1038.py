lista = input().split()

codigo = int(lista[0])
quantidade = int(lista[1])

if codigo == 1:
    total_pagar = quantidade * 4.0
    print('Total: R$ %.2f' %total_pagar)
    
elif codigo == 2:
    total_pagar = quantidade * 4.5
    print('Total: R$ %.2f' %total_pagar)
    
elif codigo == 3:
    total_pagar = quantidade * 5.0
    print('Total: R$ %.2f' %total_pagar)

elif codigo == 4:
    total_pagar = quantidade * 2.0
    print('Total: R$ %.2f' %total_pagar)

elif:
    total_pagar = quantidade * 1.50
    print('Total: R$ %.2f' %total_pagar)
