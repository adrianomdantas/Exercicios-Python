alunos = []
todosalunos = []
while True:
    nome = (str(input('Nome: ')))
    n1 = (float(input('Nota1: ')))
    n2 = (float(input('Nota2: ')))
    notas = (n1, n2)
    alunos.append(nome)
    alunos.append(notas)
    todosalunos.append(alunos[:])
    alunos.clear()
    opcao = str(input('Deseja cadastrar outro aluno: [S/N]')).upper()
    while True:
        if opcao not in 'SN':
            opcao = str(input('Deseja cadastrar outro aluno: [S/N]')).upper()
        else:
            break
    if opcao == 'N':
        break
print(20 * '-=')
print(f'{"No":<5}{"NOME":<10}{"MEDIA":5}')
for i in range(0, len(todosalunos)):
    print(f'{i:<5}{todosalunos[i][0]:<10}{(todosalunos[i][1][0]+todosalunos[i][1][1])/2:>5.1f}')

print(40 * '-')
while True:
    naluno = int(input('Digite o No do aluno para ver suas notas: [999 para sair] '))
    if naluno == 999:
        break
    elif naluno >= len(todosalunos):
        while True:
            print('Aluno não cadastrado')
            naluno = int(input('Digite o No do aluno para ver suas notas: [999 para sair] '))
            if naluno == 999:
                break
            
    else:
        print (f'As notas do aluno {todosalunos[naluno][0]} foram {todosalunos[naluno][1]} ')
        print(40 * '-')
    if naluno == 999:
        break
print('FINALIZANDO ...')
print('<<< VOLTE SEMPRE >>>')

