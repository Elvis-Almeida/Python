#analizador completo
from datetime import date
ano = date.today().year
ti = 0
mv = 0
c = 0
for r in range(1,5):
    n = str(input('Digite o nome da {}ª pessoa: '.format(r))).strip().upper()
    i = int(input('Digite a idade da {}ª pessoa: '.format(r)))
    sexo = str(input('Digite o sexo da {}ª pessoa (Homen ou Mulher): '.format(r))).strip().upper()
    ti += i
    if sexo == 'HOMEN' and mv < i:
        mv = i
        maisvelho = n
    elif sexo == 'MULHER' and i < 20:
        c += 1
    else:
        print('Digite Homen ou Mulher')
    print('-='*20)
print('A idade media do grupo é {}'.format(ti/4))
print('O homen mais velhor é {}'.format(maisvelho))
print('No seu grupo há {} mulheres com menos de 20 anos'.format(c))