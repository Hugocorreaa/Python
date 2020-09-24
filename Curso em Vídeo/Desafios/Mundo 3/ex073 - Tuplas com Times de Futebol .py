'''

Crie uma tupla preenchida com os 20 primeiros colocados da Tabelo do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time da chapecoense.


'''

tabela = ('Atlético-MG', 'Internacional', 'São Paulo', 'Palmeiras', 'Vasco', 'Flamengo', 'Santos', 'Fortaleza',
          'Fluminense', 'Sport', 'Ceará', 'Grêmio', 'Corinthians', 'Atlético-GO', 'Athletico-PR', 'Coritiba',
          'Bragantino', 'Botafogo', 'Bahia', 'Goiás')

print('-' * 50)
print(f'Lista de times do Brasileirão: {tabela}')
print('-' * 50)
print(f'Os 5 primeiros são: {tabela[:5]}')
print('-' * 50)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('-' * 50)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-' * 50)
if tabela.count("Chapecoense") <= 0:
    print(f'O Chapecoense não está entre os 20 colocados do Brasileirão.')
else:
    print(f'O Chapecoense está na {tabela.count("Chapecoense")+1}ª posição.')

