l = []
d = []
s = c1 = c2 = 0
for c in range(0,9):
    d.append(int(input(f'Digite o numero da posicão {c1}, {c2} ')))
    c2 += 1
    if c == 2 or c == 5 or c == 8:
        c1 += 1
        c2 = 0
        l.append(d[:])
        d.clear()
print('\033[1;32m==' * 20)
for l1 in l:
    print('         ', end='')
    for n in l1:
        if n % 2 == 0:
            s += n
        print(f'[{n:^5}]', end='')
    print()
print('\033[1;32m==\033[m' * 20)
print(f'A soma de todos numeros pares é {s}')
print(f'A soma da coluna 2 é {l[0][2]+l[1][2]+l[2][2]}')
print(f'O maior valor da linha 1 é {max(l[1])}')