#gerador de cartela MEGA SENA
from random import randint
from time import sleep
p = []
r = []
y = 0
q = int(input('Quantos jogos quer gerar? '))
for c in range(0, q):
    while y <= 5:
        i = randint(1, 60)
        if i not in r:
            r.append(i)
            y += 1
        r.sort()
    p.append(r[:])
    r.clear()
    y = 0
for t, v in enumerate(p):
    print(f'Jogo {t+1}: {v}')
    sleep(1)
print(f'{"< Boa sorte >":=^40}')