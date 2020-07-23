notas = input().split()
nota1 = float(notas[0])
nota2 = float(notas[1])
nota3 = float(notas[2])
nota4 = float(notas[3])

media_notas = ((nota1*2) + (nota2*3) + (nota3*4) + (nota4 *1))/10
print('Media: %.1f'%media_notas)

if media_notas >= 7.0:
    print('Aluno aprovado.')
    
elif media_notas < 5.0:
    print('Aluno reprovado.')

else:
    print('Aluno em exame.')
    nota_exame = float(input())
    print('Nota do exame: %.1f' %nota_exame)
    media_final = (media_notas + nota_exame)/2
    if media_final > 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f' %media_final)
