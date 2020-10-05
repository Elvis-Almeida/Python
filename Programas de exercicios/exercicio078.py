m = []
n1 = []
n2 = []
for c in range(0,5):
    m.append(input(f'digite o  numero na posição {c}: '))
print(f'Sua lista foi {m}')
c = 0
for r in m:
    if c == 0:
        maior = int(r)
        menor = int(r)
    else:
        if maior < int(r):
            maior = int(r)
        elif menor > int(r):
            menor = int(r)
    c += 1
n1.append(m.index(str(maior)))
if m.count(str(maior)) > 1:
    corretor = m.index(str(maior))+1
    daliprafrente = m.index(str(maior))+1
    num = m[daliprafrente:].index(str(maior)) + corretor
    n1.append(num)
if m.count(str(maior)) > 2:
    num = m[num:].index(str(maior)) + corretor + 1
    n1.append(num)
if m.count(str(maior)) > 3:
    num = m[num:].index(str(maior)) + corretor + 2
    n1.append(num)
if m.count(str(maior)) > 4:
    num = m[num:].index(str(maior)) + corretor + 3
    n1.append(num)

#para saber o menor
n2.append(m.index(str(menor)))
if m.count(str(menor)) > 1:
    corretor = +1
    daliprafrente = m.index(str(menor))+1
    num = m[daliprafrente:].index(str(menor)) + corretor
    n2.append(num)
if m.count(str(menor)) > 2:
    num = m[num:].index(str(menor)) + corretor + 1
    n2.append(num)
if m.count(str(menor)) > 3:
    num = m[num:].index(str(menor)) + corretor + 2
    n2.append(num)
if m.count(str(menor)) > 4:
    num = m[num:].index(str(menor)) + corretor + 3
    n2.append(num)

print(f'O numero maior foi {maior} e estão nas posições: {n1}')
for i, v in enumerate(m):
    if v == str(maior):
        print(i, end='')
print()
print(f'O numero menor foi {menor} e estão nas posições: {n2}')
for i, v in enumerate(m):
    if v == str(menor):
        print(i, end='')
print()