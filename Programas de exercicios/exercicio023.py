#mostrar os numeros de 0 a 9999 separados
n = input('digite um numero de 0 a 9999: ')
q = '{:0>4}'.format(n)
print('milhares {}\ncentenas {}\ndezenas  {}\nunidades {}'.format(q[0],q[1],q[2],q[3]))

ab = int(input('digite outro numero: '))
a = ab//1 % 10
b = ab//10 % 10
c = ab//100 % 10
d = ab//1000 %10
print('unidade {}\ndezena  {}\ncentena {}\nmilhar  {}'.format(a,b,c,d))