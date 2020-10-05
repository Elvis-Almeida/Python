#matriz 3X3 melhorada
l1 = []
l2 = []
l3 = []
d = []
s = 0
t1 = 0
t2 = 0
for c in range(0,9):
    p = int(input(f'Digite o numero da posicão {t2}, {t1} '))
    if c == 2 or c == 5 or c == 8:
        t2 += 1
    if t1 < 2:
        t1 += 1
    else:
        t1 = 0
    if p % 2 == 0:
        s += p
    d.append(p)
    if c < 3:
        l1.insert(c, d[:])
    elif 2 < c < 6:
        l2.insert(c, d[:])
    elif 5 < c:
        l3.insert(c, d[:])
    d.clear()
print('\033[1;32m==' * 20)
print('            ', l1[0], l1[1], l1[2])
print('            ', l2[0], l2[1], l2[2])
print('            ', l3[0], l3[1], l3[2])
print('==' * 20)
print(f'\033[mA soma de todos numeros pares são {s}')
print(f'A soma dos numeros da coluna 2 é {l1[2][0]+l2[2][0]+l3[2][0]}')
print(f'O maior valor da linha 1 é {max(l2[:])}')