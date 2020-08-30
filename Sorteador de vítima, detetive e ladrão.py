from random import randint
from os import system

listafinal = []
listainicial = []
d = []
F = False

def lerint(txt):
    while True: 
        a = input(txt)
        if len(a) == 0:
            a = 'a'
            
        if a in '1234567890':
            return int(a)
            break 
        else:
            print('\033[1;31mdigite um numero\033[m')

def vitima():
    for c in range(0, vítima):
        listainicial.append('Vítima')

def ladrao():
    for c in range(0, ladrão):
        listainicial.append('Ladrão')

def detet():   
    for c in range(0, detetive):
        listainicial.append('Detetive')

system('cls')
print('-'*50)
vítima = lerint('Digite a quantidade de vítimas: ')
system('cls')
print('-'*50)
ladrão = lerint('Digite a quantidade de ladrões: ')
system('cls')
print('-'*50)
detetive = lerint('Digite a quantidade de detetives: ')
print('-'*50)

s = 0

for c in range(0,3):
    while True:
            numero = randint(0, 2)
            if s == 0:
                s += 1
                if numero == 0:
                      vitima()
                if numero == 1:
                      detet()
                if numero == 2:
                      ladrao()
                d.append(numero)
                break
            else:
                for c in d:
                    if numero == c:
                        F = False
                        break
                    elif numero != c:
                        F = True
                if F:
                    s += 1
                    d.append(numero)
                    if numero == 0:
                          vitima()
                    if numero == 1:
                          detet()
                    if numero == 2:
                          ladrao()
                    break    
d.clear()
total = ladrão + detetive + vítima
p = 0
for c in range(0, total):
    while True:
        numero = randint(0, total-1)
        if p == 0:
            p += 1
            d.append(numero)
            listafinal.append(listainicial[numero])
            break
        else:
            for c in d:
                if numero == c:
                    F = False
                    break
                elif numero != c:
                    F = True
            if F:
                p += 1
                d.append(numero)
                listafinal.append(listainicial[numero])
                break
m = 0
for c in listafinal:
    m += 1
    input('             Pressione Enter')
    system('cls')
    for d in range(0,6):
        print('\033[m')
    print('\033[1;36m')
    if c == 'detetive':
        print('               ',c)
    else:
        print('                ',c)
    print('\033[m')
    for c in range(0,5):
        print('\033[m')
    print()
    if m == len(listafinal):
        input('            Você foi o Ultimo')
        break
    else:
        input('             Pressione Enter')
    system('cls')
    for r in range(0,100):
        print()
system('cls')