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
        listainicial.append('vítima')

def ladrao():
    for c in range(0, ladrão):
        listainicial.append('ladrão')

def detet():   
    for c in range(0, detetive):
        listainicial.append('detetive')

vítima = lerint('Digite a quantidade de vítimas')

ladrão = lerint('Digite a quantidade de ladrões')

detetive = lerint('Digite a quantidade de detetives')

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
                    
'''for c in range(0, vítima):
    listainicial.append('vítima')

for c in range(0, ladrão):
    listainicial.append('ladrão')
    
for c in range(0, detetive):
    listainicial.append('detetive')'''
    
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
#print(listafinal)
for c in listafinal:
    m += 1
    input('             Pressione Enter')
    system('clear')
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
        exit()
    else:
        input('             Pressione Enter')
    system('clear')
    for r in range(0,100):
        print()
   
    
