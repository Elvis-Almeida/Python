#calculando uma PA
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 10
s = n
while c > 0:
    print('{}'.format(s), end = '')
    print(' >>' if c > 1 else '...', end = ' ')
    c -= 1
    s += r