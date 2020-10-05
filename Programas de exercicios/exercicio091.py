#sorteando e organizando dicionario
from time import sleep
from random import randint
from operator import itemgetter
d = dict()
f = list()
c = 0
for a in range(1,5):
    d[f'Jogador {a}'] = randint(1, 6)
for k, v in d.items():
    print(f'{k} tirou {v}')
    sleep(1)
print('=-' * 20)
f = sorted(d.items(), key=itemgetter(1), reverse=True)
print(f'{" Ranking ":-^40}')
for i, v in enumerate(f):
    print(f'        {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)