#calcule a hipotenusa do triangulo
from math import hypot
c1 = float(input('digite o cateto adjacente: '))
c2 = float(input('digite o cateto oposto: '))
h = hypot(c1,c2)
print('a hipotenusa do seu triangulo-retangulo é {}'.format(h))