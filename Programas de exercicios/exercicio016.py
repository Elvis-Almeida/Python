#transforme qualquer numero real para inteiro
from math import trunc
n1 = float(input('digite um numero real'))
n2 = trunc(n1)
print ('seu numero real {} transformado em inteiro fica {}'.format(n1,n2))