#quem tem o maior peso
M = 0
m = 0
for r in range(1,6):
    p = float(input('Digite o peso da {}ª pessoa'.format(r)))
    if r == 1:
        m = p
        M = p
    else:
        if p > M:
            M = p
        elif p < m:
            m = p
print('O maoir peso foi {}Kg e o menor foi {}Kg'.format(M, m))