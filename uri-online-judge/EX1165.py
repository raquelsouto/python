cont_primo = valor = 0
cont = cont_rep = 1

rep = int(input())
if 1 <= rep <= 100:
    while cont_rep <= rep:
        valor = int(input())
        if 1 < valor <= 10**7:
            while cont <= valor: 
                if valor % cont == 0:
                    cont_primo += 1
                cont += 1

            if cont_primo > 2:
                print('%d nao eh primo'%valor)
            else: 
                print('%d eh primo'%valor)
            cont_rep += 1
            cont = 1
            cont_primo = 0