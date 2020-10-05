import math
#calcular o seno o cosseno e a tangente de qual quer angulo 
n = int(input('digite um numero: '))
print('o seno de {} é {:.2f}\no cosseno de {} é {:.2f}\na tangente de {} é {:.2f}'.format(n,math.sin(math.radians(n)),n,math.cos(math.radians(n)),n,math.tan(math.radians(n))))
