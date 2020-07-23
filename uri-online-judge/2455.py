valores = input().split()

peso1 = int(valores[0])
comprimento1 = int(valores[1])
peso2 = int(valores[2])
comprimento2 = int(valores[3])


if 10 <= peso1 <= 100 and 10 <= comprimento1 <= 100 and 10 <= peso2 <= 100 and 10 <= comprimento2 <= 100:
    direito = peso1 * comprimento1
    esquerdo = peso2 * comprimento2

    if direito == esquerdo:
        print('0')
    elif direito < esquerdo:
        print('1')
    else:
        print('-1') 
