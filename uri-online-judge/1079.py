n = int(input())
cont_media = 0
cont_print = 0

lista_medias = []

while cont_media < n:
    nota1, nota2, nota3 = map(float, input().split())
    media = (nota1*2 + nota2*3 + nota3*5)/10
    lista_medias.append(media)
    cont_media += 1

while cont_print < n:
    print('%.1f' %lista_medias[cont_print])
    cont_print += 1