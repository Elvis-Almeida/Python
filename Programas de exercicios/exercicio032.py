#calcula se um ano é ou não bisexto
from datetime import date
ano = int(input('digite um ano,ou digite 0 para analizar seu ano'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Seu ano {} é Bisexto'.format(ano))
else:
    print('Seu ano {} não é Bisexto'.format(ano))