n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 10
s = n
p = 1
soma = 0
while p > 0:
    soma += c
    while c > 0:
        print('{}'.format(s), end = '')
        print(' >>' if c > 1 else '...', end = ' ')
        c -= 1
        s += r
    p = c = int(input('\nDigite quantos numeros a mais voçê quer ver: '))
print('Foi mostrado um total de {} Termos'.format(soma))
