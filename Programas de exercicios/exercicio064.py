#somando até quando quiser
para = s = c = 0
while para != 1000:
    n = int(input('Digite o numero a ser somado[999 para]: '))
    if n == 1000:
        para = n
    else:
        s += n
        c += 1
print('A soma de todos os {} numeros digitados é {}'.format(c,s))