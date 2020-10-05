#quantoas pesosas tem maior idade
from datetime import date
ano = date.today().year
m = 0
M = 0
for r in range(1, 8):
    n = int(input('Digite o ano de nascimento da {}ª pessoa'.format(r)))
    f = ano - n
    if f < 21:
        m += 1
    elif f >= 21:
        M += 1
print('Voçê tem {} menor de idade e {} maior de idade'.format(m,M))
