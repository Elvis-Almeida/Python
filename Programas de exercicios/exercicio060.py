#calculando fatorial
'''import math
n = int(input('Digite um valor: '))
print('Seu fatorial é {}'.format(math.factorial(n)))'''

n1 = int(input('Digite um valor: '))
n = n1
r = 1
c = n1
print('Calculando...')
print('{}! = '.format(n1), end = '')
while n > 0:
   print(c, end = ' ')
   print('x 'if c > 1 else '= ', end = '')
   c -= 1
   r = r * n
   n = n - 1
print(r)