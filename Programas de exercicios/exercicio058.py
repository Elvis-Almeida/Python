#jogo melhorado exercicio28
from random import randint
from time import sleep
q = 0
n = 1
c = 0
n = randint(0,10)#escolhendo o numero aleatorio
print('\033[1;34m>>>>' * 10)
print('\033[1;30mtente acertar um numero de 0 a 10')
print('\033[1;34m<<<<' * 10)
while q != n:
    q = int(input('''\033[1;30mque numero voçê pensou? '''))#jogador escolhendo um numero
    print("Processando...")
    sleep(1)#fazer o computador esperar um tempo
    c += 1
    if n == q:
        print('\033[1;32mvoçê VENCEU!')
    elif n > q:
        print('\033[1;31mTente um numero maior!')
    elif n < q:
        print('\033[1;31mTente um numero menor!')
print('Voçê precisou de {} temtativas para vencer'.format(c))
