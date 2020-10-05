#matriz 3X3
l1 = []
l2 = []
l3 = []
d = []
for c in range(0,3):
    d.append(input(f'Digite o numero da posicão 0, {c} '))
    l1.insert(c, d[:])
    d.clear()
for c in range(0, 3):
    d.append(input(f'Digite o numero da posição 1, {c} '))
    l2.insert(c, d[:])
    d.clear()
for c in range(0, 3):
    d.append(input(f'Digite o numero da posição 2, {c} '))
    l3.insert(c, d[:])
    d.clear()
print(l1)
print(l2)
print(l3)