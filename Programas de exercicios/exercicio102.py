#calculo do fatorial
def fatorial(n, show=False):
    '''
    A função calcula o fatorial do numero informado
    :param n: numero a ser calculado o fatorial
    :param show: mostra por completo a operação (False por padrão)
    :return: retorna o fatorial de n
    '''
    s = n
    for c in range(n,1,-1):
        if show:
            print(c ,end='')
            if c > 2:
                print(end=' X ')
            else:
                print(end=' X 1 = ')
        s *= c-1
    return s


#Programa principal
s = fatorial(int(input('Digite um numero')), True)
print(s)