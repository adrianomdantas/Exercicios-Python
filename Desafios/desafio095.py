jogadores = list()
gols = list()
jogador = dict()

while True:
    jogador['nome'] = str(input('Nome: '))
    qtd_partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    for i in range(0, qtd_partidas):
        gols.append(int(input(f'Gols na partida {i}: ')))
    jogador['gols'] = gols.copy()
    gols.clear()
    jogadores.append(jogador.copy())
    opcao = str(input('Deseja cadastrar outro jogador? [S/N] ' )).strip().upper()
    print(40 * '-')
    while True:
        if opcao not in 'SN':
            opcao = str(input('!ERR!\nDeseja cadastrar outro jogador? [S/N] ' )).strip().upper()            
        else:
            break
    if opcao == 'N':
        break
print(jogadores)



