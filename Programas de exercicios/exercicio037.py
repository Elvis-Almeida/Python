#comversor para binario, octa e hexadecimal
print('\033[1;30mComverssor')
print('\033[32m§§'*14)
print('\033[1;34mdigite 1 para binario\ndigite 2 para octa\ndigite 3 para hexadecimal\033[m')
print('\033[32m§§\033[m'*14)
v = int(input("digite para qual deseja converter"))
if v == 1:
    n = int(input('digite o numero a ser convertido para binário'))
    r = bin(n)
    c = 'binário'
elif v == 2:
    n = int(input('digite o numero a ser convertido para octa'))
    r = oct(n)
    c = 'octa'
elif v == 3:
    n = int(input('digite o numero a ser convertido para hexadecimal'))
    r = hex(n)
    c = 'hexadecimal'
if v == 1 or v == 2 or v == 3:
    r = r[2:]
    print('\033[35m**\033[m'*40)
    print('\033[1;30mSeu numero {} Comvertido para {} é {}'.format(n,c,r))
    print('\033[35m**\033[m'*40)
else:
    print('\033[1;31mNUMERO ERRADO! Digite 1, 2 ou 3\n      Tente Novamente!!')