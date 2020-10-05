import random
def sortear(numeros):
    f = []
    for c in range(0, 5):
        n = random.choice(numeros)
        f.append(n)
        numeros.remove(n)
    numeros.clear()
    numeros.append(f[:])


def somapar(numeros):
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(soma)


numeros = list()
while True:
    add = int(input('Digite um numero: '))
    numeros.append(add)
    cont = str(input('Quer continuar? S/N'))[0].strip().upper()
    if cont in 'N':
        break
sortear(numeros)
print(numeros[0])
print(f'A soma dos numeros pares é', end=' ')
somapar(numeros[0])