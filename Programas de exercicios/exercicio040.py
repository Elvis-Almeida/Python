#cauculando a media e sua situação
print('sua nota deve ir de 0 a 10')
n1 = float(input('Digite sua 1º nota'))
n2 = float(input('Digite sua 2º nota'))
m = (n1+n2)/2
if 10.111 > m >= 7 and n1 < 10.111 and n2 < 10.111:
    print('\033[1;32mVocê foi APROVADO')
    print(' Sua media é {:.1f}'.format(m))
elif 7 > m >=5 and n1 < 10.111 and n2 < 10.111:
    print('\033[1;33mVoçê está de RECUPERAÇÃO')
    print('    Sua media é {:.1f}'.format(m))
elif 0 < m < 5 and n1 < 10.111 and n2 < 10.111:
    print('\033[1;31mVoçê REPROVOU DIRETO')
    print('  Sua media é {:.1f}'.format(m))
elif n1 > 10 or n2 > 10 or n1 < 0 or n2 < 0:
    print('\033[1;31mseu numero foi maior que 10 ou menor que 0. Tente novamente!!')