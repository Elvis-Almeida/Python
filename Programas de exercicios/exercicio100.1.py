import random
from time import sleep


def sortear(numeros):
    print('Sorteando:', end=' ')
    for c in range(0, 5):
        n = random.randint(0,10)
        print(n, end=' ')
        sleep(0.3)
        numeros.append(n)
    print('Pronto!')


def somapar(numeros):
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos numeros pares de {numeros} é {soma}')


#PROGRAMA PRINCIPAL
numeros = []
sortear(numeros)
somapar(numeros)