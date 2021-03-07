times = ('Palmeiras', 'Flamengo', 'Internacional', 'Gremio', 'São Paulo', 'Atletico - MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceara SC', 'Vasco da Gama', 'Sport Recife', 'America-MG', 'EC Vitória', 'Paraná')
print(f'A) Os 5 primeiros são {times[:5]}')
print(f'B) Os 4 ultimos são {times[-4:]}')
print('C) times em ordem alfabetica ', (sorted(times)))
print('D) A Chapecoense está na posição {}'.format(times.index('Chapecoense')+1))

