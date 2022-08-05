def titulo(msn):
    print(40 * '-')
    print(f'{msn:^40}')
    print(40 * '-')
def consulta():
    titulo('PESSOAS CADASTRADAS')
    with open('pessoas.txt', 'r', encoding='UTF-8') as arquivo:
        pessoas = arquivo.readlines()
    #print(pessoas)
    for p, linha in enumerate(pessoas):
        linha = linha.rstrip()
        print(linha)

def adicionar():
    titulo('NOVO CADASTRO')
    nome = input('Digite: ')
    idade = int(input('Digite a idade: '))
    with open('pessoas.txt', 'a') as arquivo:
        arquivo.write(f'\n{nome:<25}{idade:>10}{"anos":>5}') 



while True:
    titulo('MENU PRINCIPAL')
    print('\033[0;0;33m1\033[0;0;34m - Ver pessoal cadastrado\033[m')
    print('\033[0;0;33m2\033[0;0;34m - Cadastrar novas Pessoas\033[m')
    print('\033[0;0;33m3\033[0;0;34m - Sair do Sistema\033[m')
    print(40 * '-')
    opcao = int(input('Sua Opção: '))
    if opcao not in [1, 2, 3]:
        print('digitou errado')
    elif opcao == 1:
        consulta()
    elif opcao == 2:
        adicionar()
    elif opcao == 3:
        break
titulo('FIM')

