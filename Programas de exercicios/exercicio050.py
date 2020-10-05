#le 6 numeros e somar os pares
s = 0
cont = 0
for c in range(0, 6):
    n = int(input('digite um numero: '))
    if n % 2 == 0:
        cont += 1
        s += n
print('a soma dos {} numeros pares é {}'.format(cont, s))