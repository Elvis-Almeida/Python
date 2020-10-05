from random import randint
numeros = (randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),)
print(f'Os numeros gerados foram:', end=' ')
for g in numeros:
    print(f'{g}', end=' ')
n = 0
'''for c in range(0,5): #para saber o maior e o menor
    n += 1
    if n == 1:
        maior = numeros[c]
        menor = numeros[c]
    else:
        if maior < numeros[c]:
            maior = numeros[c]
        if menor > numeros[c]:
            menor = numeros[c]'''
#ou
print(f'\nO maior numero gerado foi {max(numeros)} \nO menor numero gerado foi {min(numeros)}')