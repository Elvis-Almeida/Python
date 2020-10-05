l = []
d = []
c1 = c2 = 0
for c in range(0,9):
    d.append(input(f'Digite o numero da posicão {c1}, {c2} '))
    c2 += 1
    if c == 2 or c == 5 or c == 8:
        c1 += 1
        c2 = 0
        l.append(d[:])
        d.clear()
for l1 in l:
    for n in l1:
        print(f'[{n:^5}]', end='')
    print()
