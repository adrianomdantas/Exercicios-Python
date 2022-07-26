jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: '))
gols = list()
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
jogador['gols'] = gols
print(40 * "=-")
jogador['totgols'] = 0
for g in gols:
    jogador['totgols'] += g
    
#print(jogador) 
print(40 * "=-")
print(f'O Jogador {jogador["nome"]} jogou {partidas} partidas')
#print(jogador['gols'])
for k, v in enumerate(jogador['gols']):
    print(f'{"=>":>5} Na partida {k}, fez {v} gols.')