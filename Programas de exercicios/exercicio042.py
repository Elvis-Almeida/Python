#calculo para saber se as tres retas forman um triangulo
print('\033[1;30m```' * 10)
print('analizador de triangulos')
print('\033[1;30m´´´' * 10)
n1 = float(input('Em cm digite o tamanho da reta 1: '))
n2 = float(input('Em cm digite o tamanho da reta 2: '))
n3 = float(input('Em cm digite o tamanho da reta 3:\033[1;36m '))
if n1 < (n2+n3) and n3 < (n1+n2) and n2 < (n1+n3):
    print('Suas Retas {}, {}, {}, podem formar um triangulo: '.format(n1, n2, n3) ,end = '')
    if n1 == n2 == n3:
        print('Seu Triangulo é EQUILÁTERO')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Seu Triangulo é ISÓSCELES')
    elif n1 != n2 != n3:
        print('Seu Triangulo é ESCALENO')
else:
    print('suas retas {}, {}, {}, não forman um triangulo'.format(n1,n2,n3))