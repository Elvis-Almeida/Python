#melhorando o 093
d = {}
l = []
gols = []
total = 0
while True:
    d['Nome'] = str(input('Nome do jogador: ')).strip()
    p = int(input(f'Quantas partidas {d["Nome"]} jogou? '))
    for c in range(0,p):
        gols.append(int(input(f'Quantos gols fez na {c+1}º partida? ')))
    d['Gols'] = gols[:]
    d['Total'] = sum(gols)
    l.append(d.copy())
    d.clear()
    gols.clear()
    while True:
        cont = str(input('Adicionar mais jogadores? S/N ')).strip().upper()[0]
        if cont in 'SN':
            break
    if cont in 'N':
        break
print('=-'*30)
print('Cod ', end='')
for i in l[0].keys():
    print(f'{i:16}', end='')
print()
print('--'*25)
for c, h in enumerate(l):
    print(f'{c:^3}', end=' ')
    for k, v in h.items():
        print(f'{str(v):16}', end='')
    print()
while True:
    es = int(input('Qual jogagor quer ver mais detalhes? (888 para) '))
    if es == 888:
        break
    while es >= len(l):
        es = int(input(f'Valor {es} invalido! escolha um valor valido: '))
    print('-='*20)
    d = l[es]
    print(f'Levatamento do jogador {d["Nome"]}')
    print('-='*20)
    print(f'O jogador {d["Nome"]} jogou {p} partidas')
    for c, h in enumerate(d['Gols']):
        print(f'    => Na {c+1}º partida fez {h} gols')
    print(f'Foi um total de {d["Total"]} gols')
    print('=-'*30)
print('=-'*30)
print('Programa finalizado')