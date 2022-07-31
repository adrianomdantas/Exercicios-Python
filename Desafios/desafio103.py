def ficha(nome='<desconhecido>', g=0):
    if len(nome) == 0:
        nome = '<desconhecido>'
    if len(g) == 0:
        g = 0   
    return f'O jogador {nome} fez {g} gols'

jogador = str(input('Nome do Jogador: '))
gols = input('Gols: ')
print(ficha(jogador, gols))