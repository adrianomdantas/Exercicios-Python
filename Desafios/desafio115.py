def titulo(msn):
    print(40 * '-')
    print(f'{msn:^40}')
    print(40 * '-')

def consulta():
    titulo('PESSOAS CADASTRADAS')
    with open('pessoas.txt', 'r', encoding='UTF-8') as arquivo:
        pessoas = arquivo.readlines()
    print(pessoas)
    for p, linha in enumerate(pessoas):
        linha = linha.rstrip()
        print(p, linha)   
def adicionar():
    titulo('NOVO CADASTRO')
    adic = input('Digite: ')
    with open('pessoas.txt', 'a') as arquivo:
        arquivo.write(f'\n{adic}') 
titulo('MENU PRINCIPAL')
print('\033[0;0;33m1\033[0;0;34m - Ver pessoal cadastrado\033[m')
print('\033[0;0;33m2\033[0;0;34m - Cadastrar novas Pessoas\033[m')
print('\033[0;0;33m3\033[0;0;34m - Sair do Sistema\033[m')
print(40 * '-')
opcao = int(input('Sua Opção: '))

consulta()
adicionar()
consulta()
