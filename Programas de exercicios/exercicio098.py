#contador em função
from time import sleep


def contador(c, f, d):
    l = []
    com = c
    fim = f
    de = d
    if d == 0:
        d = 1
    if c > f:
        if d > 0:
            while c >= f:
                l.append(f)
                f += d

            l.reverse()
        else:
            d = d*-1
            while c >= f:
                l.append(f)
                f += d
            l.reverse()
    else:
        if d < 0:
            d = d*-1
            while f >= c:
                l.append(c)
                c += d
        else:
            while f >= c:
                l.append(c)
                c += d
    print(f'Comtador de {com} até {fim} de {d} em {d}')
    for c in l:
        #flush para eliminar o bug de tela demorar aparecer
        print(c, end=' ', flush=True)
        sleep(0.25)
    print()

#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('=-' * 30)
print('Agora é com voçê!')
c = int(input('começo: '))
f = int(input('Final: '))
d = int(input('De: '))
print('=-'*30)
contador(c, f, d)