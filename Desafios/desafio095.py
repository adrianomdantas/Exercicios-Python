jogadores = list()
gols = list()
jogador = dict()

while True:
    print(40 * '-')
    jogador['nome'] = str(input('Nome do Jogador: '))
    qtd_partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    for i in range(0, qtd_partidas):
        print('', end="   ")
        gols.append(int(input(f'Gols na partida {i}: ')))
    jogador['gols'] = gols.copy()
    gols.clear()
    jogadores.append(jogador.copy())
    opcao = str(input('Deseja cadastrar outro jogador? [S/N] ' )).strip().upper()
    
    while True:
        if opcao not in 'SN':
            opcao = str(input('!ERRO!\nDeseja cadastrar outro jogador? [S/N] ' )).strip().upper()            
        else:
            break
    if opcao == 'N':
        break
#print(20 * '=-')
#print(jogadores)
#print(20 * '=-')

for i in jogadores:
    i['totgols'] = 0
    for j in i['gols']:
        i['totgols'] += j

print(40 * '-')    
print(f'{"cod":>4} {"Nome":<15} {"Gols":<15} {"Total":<25}')
print(40 * '-')

for p, i in enumerate(jogadores):
    print(f'{p:>4} {i["nome"]:<15} {str(i["gols"]):<15} {i["totgols"]:<15}')
#print(jogadores)

print(40 * '-')

while True:
    print(40 * '-')
    dadosj = int(input('Mostrar dados de qual jogador? 999 para sair: '))
    if dadosj >= len(jogadores) and dadosj != 999:
        while True:
            if dadosj >= len(jogadores) and dadosj != 999:
                print('!ERRO! este jogador não existe')
                break
            else:
                break
    else:
        print(20 * '=-')
        for p, d in enumerate(jogadores):
            if p == dadosj:
                print(f'Levantamento dos dados do jogador {d["nome"]}')
                for t, u in enumerate(d['gols']):
                    print('  ', end=' ')
                    print(f'Na partida {t} fez {u} gols')
                
    if dadosj == 999:
        break
print('<< FIM >>')
    



