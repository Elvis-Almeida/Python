#calculo para saber se as tres retas forman um triangulo
print('```' * 10)
print('analizador de triangulos')
print('´´´' * 10)
n1 = float(input('Em cm digite o tamanho da reta 1: '))
n2 = float(input('Em cm digite o tamanho da reta 2: '))
n3 = float(input('Em cm digite o tamanho da reta 3: '))
m1 = (n2-n3)
m2 = (n1-n2)
m3 = (n1-n3)
if m1 < 0:
    m1 = m1 * -1
if m2 < 0:
    m2 = m2 * -1
if m3 < 0:
    m3 = m3 * -1
if m1 < n1 < (n2+n3) and m2 < n3 < (n1+n2) and m3 < n2 < (n1+n3):
    print('Suas Retas {}, {}, {}, podem formar um triangulo:'.format(n1,n2,n3))
else:
    print('suas retas {}, {}, {}, não forman um triangulo'.format(n1,n2,n3))



