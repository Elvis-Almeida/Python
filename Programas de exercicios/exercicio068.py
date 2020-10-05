#joguinho par ou inpar
from random import randint
c = 0
print('\033[1;36m{:~^40}'.format(" impar pa "))
while True:
    pc = randint(0,9)
    j = int(input('Digite seu numero: '))
    pi = str(input('Voçê quer par[P] ou impar[I]?')).strip()
    while pi[0] not in 'iIpP':
        pi = str(input('Voçê quer par[P] ou impar[I]?')).strip()
    s = j + pc
    print('=-' * 20)
    print(f'O PC escolheu {pc} e voçê {j} a soma deu {s} que é ',end='')
    print('PAR' if s % 2 == 0 else 'IMPAR')

    if s % 2 == 0:
        if pi in 'pP':
            print('Voçê Ganhou!')
        else:
            print('Voçê PERDEU!')
            print('-=' * 20)
            break
    else:
        if pi in 'iI':
            print('Voçê Ganhou!')
        else:
            print('Voçê PERDEU!')
            print('-=' * 20)
            break
    print('-='*20)
    c += 1
print(f'Voçê teve {c} vitorias consecutivas')
