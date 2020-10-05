#se voçê pode ou não ser alistad
from datetime import date
print('\033[1;30mveja se voçê pode ou não se alistar!')
print('digite 1 para homen e 2 para mulher')
print('')
g = int(input('Que genero voçê é? '))
data = date.today().year
if g == 1:
    i = int(input('digite seu ano de nascimento:\033[m '))
    if (data - i) < 18:
        b = data + (18 - (data - i))
        print('\033[1;32mVoçê esta novo para se alistar espere até {} para ter 18 anos '.format(data + (18 - (data - i))))
    elif 17< (data - i) < 19:
        print('\033[1;32mvoçê esta na idade de se alistar')
    else:
        a = date.today().year - (((data-i)-18))
        print('\033[1;32mvoçê ja passou {} Ano(s) do tempo de se alistar\nEra pra ter se alistado em {} '.format(((date.today().year-i)-18),a))
elif g == 2:
        print('voçê não precisa se alistar no exercito')
else:
    print('\033[1;31mdigite 1 ou 2, e tente novamente')