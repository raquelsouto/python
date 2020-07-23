lista_num = []
cont = n = 0 
while cont < 100:
    n = int(input())
    lista_num.append(n)
    cont += 1
    
maior = max(lista_num)
print('%d' %maior)

posicao = lista_num.index(maior) + 1
print('%d' %posicao)