cont = soma = cont_notas = n = 0
opcao = 1

while opcao != 2:
    if opcao == 1:
        while cont_notas < 2:
            n = float(input())
            if 0 <= n <= 10:
                soma += n
                cont_notas += 1  
            else:
                print('nota invalida')
                cont += 1
        media = soma/2
        print('media = %.2f' %media)

        cont_notas = 0
        soma = 0
    opcao = int(input('novo calculo (1-sim 2-nao)\n'))

