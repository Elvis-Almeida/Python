d = {}
gols = []
total = 0
d['Nome'] = str(input('Nome do jogador: ')).strip()
p = int(input(f'Quantas partidas {d["Nome"]} jogou? '))
for c in range(0,p):
    gols.append(int(input(f'Quantos gols fez na {c+1}º partida? ')))
d['Gols'] = gols[:]
d['Total'] = sum(gols)
print('-='*20)
print(d)
print('-='*20)
for k, v in d.items():
    print(f'O campo {k} tem o valor  {v}')
print('-='*20)
print(f'O jogador jogou {p} partidas')
for c, h in enumerate(d['Gols']):
    print(f'    => Na {c+1}º partida fez {h} gols')
print(f'Foi um total de {d["Total"]} gols')