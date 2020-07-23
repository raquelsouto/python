# -------------------------------------- IMPORTS ---------------------------
import json 
import os.path

# -------------------------------------- FUNÇÕES ---------------------------

def criar_verificar_json():
    filename = 'info_alunos.json'
    if not os.path.exists(filename):
        with open(filename, 'w') as arquivo_escrita: 
            arquivo_escrita.write('{}')

        with open(filename, 'r') as leitura_json:
            objeto_json = json.load(leitura_json)

        objeto_json["alunos"] = []
        objeto_json["notas"] = []
        objeto_json["medias"] = []

        with open(filename, 'w') as arquivo_escrita: 
            json.dump(objeto_json, arquivo_escrita, indent=4)

def adicionar_aluno(aluno):
    if aluno not in alunos_nomes:
        alunos_nomes.append(aluno)
        alunos_notas.append([-1,-1,-1])
        alunos_medias.append(-1)
    else:
        print('Esse aluno já foi adicionado')

def adicionar_nota(aluno, nota):
    if aluno in alunos_nomes:
        ind_aluno = alunos_nomes.index(aluno)
        notas_do_aluno = alunos_notas[ind_aluno]
        if -1 in notas_do_aluno:
            index_nota_livre = notas_do_aluno.index(-1)
            notas_do_aluno[index_nota_livre] = nota
        
        elif 1 < notas_do_aluno > 3: 
            print('Inválido. Escolha a 1, 2 ou 3 nota')
        
        else:
            print('Não foi possível adicionar a nota, pois as 3 notas já foram preenchidas.')
    else:
        print('O aluno não foi encontrado. Adicione-o antes de adicionar uma nota.')

def remover_aluno(aluno):
    if aluno in alunos_nomes:
        ind_aluno = alunos_nomes.index(aluno)
        nome_aluno = alunos_nomes.pop(ind_aluno)
        notas_do_aluno = alunos_notas.pop(ind_aluno)
        media_do_aluno = alunos_medias.pop(ind_aluno)
    else:
        print('Este aluno não foi adicionado.') 

def remover_nota(aluno, nota):
    if aluno in alunos_nomes:
        ind_nome = alunos_nomes.index(aluno)
        notas_do_aluno = alunos_notas[ind_nome]
        if notas_do_aluno[nota - 1] != -1:
            notas_do_aluno[nota - 1] = -1
        else:
            print('Esta nota não existe.')
    else:
        print('Este aluno não foi cadastrado.')

def editar_nome(aluno, novo_aluno):
    if aluno in alunos_nomes:
        ind_nome = alunos_nomes.index(aluno)
        alunos_nomes[ind_nome] = novo_aluno
    else:
        print('Este aluno não foi cadastrado, por favor, adicione-o.')

def editar_nota(aluno, ind_nota, nova_nota):
    if aluno in alunos_nomes:
        ind_nome = alunos_nomes.index(aluno)
        notas_do_aluno = alunos_notas[ind_nome]
        if notas_do_aluno[ind_nota-1] != - 1:
            notas_do_aluno[ind_nota - 1] = nova_nota
        else:
            print('Este aluno não possui essa nota cadastrada.') 

    else:
        print('Este aluno não foi adicionado, por favor, adicione-o.')

def buscar_aluno(aluno):
    encontrado = False
    aluno_minusculo = aluno.lower()
    for pos in range(0, len(alunos_nomes)):
        if (aluno in alunos_nomes[pos]) or (aluno_minusculo in alunos_nomes[pos]):
            print('Nome(s) encontrado(s): %s' %(alunos_nomes[pos]))
            encontrado = True
    
    if not encontrado:
        print("Aluno não foi encontrado.")

def check_notas_faltantes():
    notas_ok = True
    for pos in range(0, len(alunos_notas)):
        if -1 in alunos_notas[pos]:
            notas_ok = False
            print('O aluno %s possui notas faltantes.' %alunos_nomes[pos])
    return notas_ok

def calcular_media_alunos():
    if check_notas_faltantes():
        for pos in range(0, len(alunos_notas)):
            soma_notas = sum(alunos_notas[pos])
            media_cada_aluno = soma_notas/3
            alunos_medias[pos] = media_cada_aluno
        return True
    else:
        return False

def calcular_media_turma():
    if calcular_media_alunos():
        soma_todas_medias = sum(alunos_medias)
        media_geral = soma_todas_medias/len(alunos_nomes)
        print('A média da turma é %.2f' %media_geral)
    else:
        print('Não foi possível calcular a média da turma.')

def melhor_aluno():
    if calcular_media_alunos():
        maior_media = max(alunos_medias)
        ind_maior_media = alunos_medias.index(maior_media)
        print('O melhor aluno da sala é: %s. Média: %.2f' %(alunos_nomes[ind_maior_media], maior_media))

def ordenar_nomes(nomes, notas, medias):
    nomes, notas, medias = (list(t) for t in zip(*sorted(zip(nomes, notas, medias))))
    return (nomes, notas, medias)

def ordenar_notas(medias, nomes, notas):
    medias, nomes, notas = (list(t) for t in zip(*sorted(zip(medias, nomes, notas),reverse=True)))
    return(medias, nomes, notas)
#AJEITAR

def alunos_aprovados():
    if calcular_media_alunos():
        print('ALUNOS QUE FORAM APROVADOS:')
        cont = 0
        while cont < len(alunos_nomes):
            if alunos_medias[cont] >= 7:
                print('Nome: %s. Média: %.2f' %(alunos_nomes[cont],alunos_medias[cont]))
            cont += 1
        print('-=' * 30)
        print(' ')
    else:
        print('Não foi possível calcular os alunos aprovados.')

def alunos_reprovados():
    if calcular_media_alunos():
        cont = 0
        print('ALUNOS REPROVADOS:')
        while cont < len(alunos_nomes):
            if alunos_medias[cont] < 5:
                print('Nome: %s. Média: %.2f' %(alunos_nomes[cont], alunos_medias[cont]))
            cont += 1
        print('-=' * 30)
        print(' ')
    else:
        print('Não foi possível calcular os alunos reprovados.')

def alunos_final():
    if calcular_media_alunos():
        print('ALUNOS QUE FORAM PARA FINAL:')
        cont = 0
        while cont < len(alunos_nomes):
            if 5 <= alunos_medias[cont] < 7:
                print('Nome: %s. Média: %.2f' %(alunos_nomes[cont], alunos_medias[cont]))
            cont += 1
        print('-=' * 30)
        print(' ')
    else:
        print('Não foi possível calcular os alunos que vão para a final.')

# --------------- PROGRAMA PRINCIPAL -------------------------------

print('Esse sistema tem por objetivo permitir manipular nomes de alunos e suas nota')
print('''
    1. ADICIONAR ALUNO
    2. ADICIONAR NOTA
    3. REMOVER ALUNO
    4. REMOVER NOTA
    5. EDITAR NOME DE ALUNO
    6. EDITAR NOTA DE ALUNO
    7. BUSCAR NOME DE ALUNO
    8. CALCULAR MEDIA DA TURMA
    9. EXIBIR MELHOR ALUNO
    10. NOME DE ALUNO EM ORDEM ALFABETICA
    11. EXIBIR ALUNOS ORDENADOS POR NOTAS
    12. EXIBIR ALUNOS APROVADOS POR MÉDIA (>=7)
    13. EXIBIR ALUNOS NA FINAL (>= 5)
    14. EXIBIR ALUNOS REPROVADOR (>5)
    15. ENCERRA PROGRAMA
    ''')

criar_verificar_json()

filename_json = 'info_alunos.json'
with open(filename_json, 'r') as json_leitura:
    objeto_json = json.load(json_leitura)

alunos_nomes = objeto_json['alunos']
alunos_notas = objeto_json['notas']
alunos_medias = objeto_json['medias']

escolha = 0
while escolha != 15:
    escolha = int(input('Digite a opção que deseja: '))
    
    if escolha == 1:
        aluno = input('Digite o nome do aluno: ')
        adicionar_aluno(aluno)
        print(alunos_nomes)
        print(alunos_notas)
        print(alunos_medias)
        print(' ')

    elif escolha == 2:
        aluno = input('Digite o nome do aluno: ')
        if aluno in alunos_nomes:
            nota = float(input('Digite a nota do aluno: '))
            adicionar_nota(aluno, nota)
            print(alunos_nomes)
            print(alunos_notas)
        else:
            print('Não é possível adicionar a nota no aluno, pois ele não está cadastrado.')
            print(' ')

    elif escolha == 3:
        aluno = input('Digite o nome do aluno a ser removido: ')
        remover_aluno(aluno)
        print(alunos_nomes)
        print(alunos_notas)

    elif escolha == 4:
        aluno = input('Digite o nome do aluno: ')
        nota = int(input('Digite qual nota deseja remover (1, 2 ou 3): '))
        remover_nota(aluno, nota)
        print(alunos_nomes)
        print(alunos_notas)        

    elif escolha == 5:
        aluno = input('Digite o nome do aluno: ')
        novo_aluno = input('Digite o novo nome do aluno: ')
        editar_nome(aluno, novo_aluno)
        print(alunos_nomes)
        print(alunos_notas)

    elif escolha == 6:
        aluno = input('Digite o nome do aluno: ')
        ind_nota = int(input('Digita em que avaliação deseja editar (1, 2 ou 3): '))
        nova_nota = float(input('Digite a nova nota: '))
        editar_nota (aluno, ind_nota, nova_nota)
        print(alunos_nomes)
        print(alunos_notas)

    elif escolha == 7:
        alunos_nomes, alunos_notas, alunos_medias = ordenar_nomes(alunos_nomes, alunos_notas, alunos_medias)
        aluno = input('Digite o nome do aluno: ')
        buscar_aluno(aluno)

    elif escolha == 8:
        calcular_media_turma()

    elif escolha == 9:
        melhor_aluno()

    elif escolha == 10:    
        alunos_nomes, alunos_notas, alunos_medias = ordenar_nomes(alunos_nomes, alunos_notas, alunos_medias)
        cont = 0
        while cont < len(alunos_nomes):
            print('Nome do aluno: %s. Notas: %d, %d, %d. Média: %.2f'
            %(alunos_nomes[cont], alunos_notas[cont][0], alunos_notas[cont][1], alunos_notas[cont][2], alunos_medias[cont]))
            cont += 1

    elif escolha == 11:
        alunos_medias, alunos_nomes, alunos_notas = ordenar_notas(alunos_medias, alunos_nomes, alunos_notas)
        cont = 0
        while cont < len(alunos_nomes):
            print('Nome do aluno: %s. Notas: %d, %d, %d. Média: %.2f'
            %(alunos_nomes[cont], alunos_notas[cont][0], alunos_notas[cont][1], alunos_notas[cont][2], alunos_medias[cont]))
            cont += 1

    elif escolha == 12:
        alunos_aprovados()

    elif escolha == 13:
        alunos_final()

    elif escolha == 14:
        alunos_reprovados()

    elif 1 < escolha > 15:
        print('Oops.. Opção inválida!')
    
    with open(filename_json, 'w') as json_escrita:
        json.dump(objeto_json, json_escrita, indent=4)

print('Bye!')