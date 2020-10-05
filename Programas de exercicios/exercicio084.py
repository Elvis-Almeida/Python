l = []
d = []
mm = []
nn = []
while True:
    l.append(input('Nome: '))
    l.append(float(input('Peso: ')))
    d.append(l[:])
    l.clear()
    con = str(input('Quer continuar? S/N' )).strip().upper()
    while con not in 'SN':
        con = str(input('Quer continuar? S/N ')).strip().upper()
    if con in 'N':
        break
print(f'Foram cadastradas {len(d)} pessoas')
ç = 0
for p in d:
    if ç == 0:
        mm.append(p[:])
        nn.append(p[:])
        ç += 1
    else:
        if mm[0][1] < p[1]:
            mm.clear()
            mm.append(p[:])
        elif mm[0][1] == p[1]:
            mm.append(p[:])
        if nn[0][1] > p[1]:
            nn.clear()
            nn.append(p[:])
        elif nn[0][1] == p[1]:
            nn.append(p[:])
        ç += 1
print(f'o maior peso foi de', end=' ')
for m in mm:
    print(m[0], end=' ')
print(f'com o peso de', end=' ')
print(mm[0][1], 'kg', end=' ')

print(f'\no menor peso foi de', end=' ')
for n in nn:
    print(n[0], end=' ')
print(f'com o peso de', end=' ')
print(nn[0][1],'kg', end=' ')
