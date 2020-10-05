def moeda(a, b='R$'):
    c = f'{b}{a:.2f}'
    d = ''
    for b in c:
        if b == '.':
            d = d + ','
        else:
            d = d + b
    return d


def metade(a):
    a = a / 2
    return moeda(a)


def dobro(a):
    a = 2 * a
    return moeda(a)


def aumentar(a, b):
    c = a * b / 100
    c = a + c
    return moeda(c)

def diminuir(a, b):
    c = a * b / 100
    c = a - c
    return moeda(c)


def resumo(a ,b, c):
    print('-'*28)
    print(f'{"Resumo do Valor":^26}')
    print('-'*28)
    print(f'Preço analizado:    {moeda(a)}')
    print(f'Dobro do Preço:     {dobro(a)}')
    print(f'Metade do preço:    {metade(a)}')
    print(f'{b}% de aumento:     {aumentar(a, b)}')
    print(f'{c}% de redução:     {diminuir(a, c)}')
    print('-' * 28)