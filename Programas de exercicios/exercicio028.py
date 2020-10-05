#joguindo de acerta o numero
from random import randint
from time import sleep
n = randint(0,5)#escolhendo o numero aleatorio
print('>>>>' * 10)
print('tente acertar um numero de 0 a 5. Qual escolhi?')
print('<<<<' * 10)
q = int(input('''que numero voçê pensou? '''))#jogador escolhendo um numero
print("Processando...")
sleep(1)#fazer o computador esperar um tempo
if n == q:
    print('voçê VENCEU!')
else:
    print('voçê PERDEU!')
    print('o numero era {} mas voçê escolheu {}'.format(n,q))