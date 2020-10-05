#classificação de faixa etaria na natação pela idade
from datetime import date
print('Qual categoria voçê irá entrar na natação')
idade = int(input('Digite seu ano de nascimento'))
ano = date.today().year
idade = ano - idade
if 0 < idade <= 9:
    c = 'MIRIM'
elif 9 < idade <= 14:
    c = 'IMFANTIL'
elif 14 < idade <= 19:
    c = 'JUNIOR'
elif 19 < idade <= 25:
    c = 'SÊNIOR'
elif 150 > idade > 25:
    c = 'MASTER'
else:
    print('\033[1;31mVocê digitou seu ANO errado')
    c = 'INVALIDA'
print('\033[1;30mVoçê tem {} Anos'.format(idade))
print('Sua categoria será \033[1;32m{}'.format(c))
