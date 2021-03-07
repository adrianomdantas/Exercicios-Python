'''Faça um programa que leia nome e media de um aluno
guardando tambem a situação em dicionario
No final mostre o conteudo da estrutura na tela'''
aluno = {}
aluno['nome'] = str(input('Aluno: '))
aluno['media'] = float(input(f'Media do aluno {aluno["nome"]}: '))
if aluno['media'] > 6:
    aluno['situacao'] = 'aprovado'
elif aluno['media'] == 6:
    aluno['situação'] = 'recuperação'
else:
    aluno['situacao'] = 'reprovado'
for a, b in aluno.items():
    print(f'o {a} é {b}')


    

    

