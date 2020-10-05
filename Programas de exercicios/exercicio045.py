#jogo do pedra papel tizoura
import random
import time
pc = random.randint(1,3)
print('\033[1;36m=='*20)
print('{:~^40}'.format(' Jogo do Pedra Papal Tezoura '))
print('=='*20)
print('')
print('''\033[1;32m[ 1 ] pedra
[ 2 ] papel
[ 3 ] tezoura''')
print('')
jg = int(input('\033[1;34mqual vai jogar?\033[1;36m'))
print('pedra')#tempo para aparecer as palavras
time.sleep(0.5)
print('papel')
time.sleep(0.5)
print('tezoura!!')
time.sleep(0.5)
#transformando em texto
if pc == 1:
    f = 'PEDRA'
elif pc == 2:
    f = 'PAPEL'
elif pc == 3:
    f = 'TEZOURA'
if jg == 1:
    v = 'PEDRA'
elif jg == 2:
    v = 'PAPEL'
elif jg == 3:
    v = 'TEZOURA'

#posibilidades de jogadas
if pc == jg:#ENPATANDO
    t = ('EMPATOU!')
    print('''\033[1;30mO computador jogou {} e voçê jogou {}
                 Voçê {}'''.format(f, v, t))
elif pc == 1 and jg == 2:#GANHANDO
    t = ('\033[1;32mVENCEU!')
    print('''\033[1;30mO computador jogou {} e voçê jogou {}
                 Voçê {}'''.format(f, v, t))
elif pc == 2 and jg == 3:
    t = ('\033[1;32mVENCEU!')
    print('''\033[1;30mO computador jogou {} e voçê jogou {}
                 Voçê {}'''.format(f, v, t))
elif pc == 3 and jg == 1:
    t = ('\033[1;32mVENCEU!')
    print('''\033[1;30mO computador jogou {} e voçê jogou {}
                 Voçê {}'''.format(f, v, t))
elif pc == 1 and jg == 3:
    t = '\033[1;31mPERDEU!'
    print('''\033[1;30mO computador jogou {} e voçê jogou {}
                 Voçê {}'''.format(f, v, t))
elif pc == 2 and jg == 1:
    t = '\033[1;31mPERDEU!'
    print('''\033[1;30mO computador jogou {} e voçê jogou {}
                 Voçê {}'''.format(f, v, t))
elif pc == 3 and jg == 2:
    t = '\033[1;31mPERDEU!'
    print('''\033[1;30mO computador jogou {} e voçê jogou {}
                 Voçê {}'''.format(f, v, t))
else:
    v = '???'
    t = '???'
    print('\033[1;31mJogada INVALIDA. Tente Novamente!\033[;m')
