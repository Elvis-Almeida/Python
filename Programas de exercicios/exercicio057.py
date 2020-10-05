#so aceita se for m ou f
n = str(input('Digite seu sexo: [H/M]')).strip().upper()[0]
while n not in 'HM':
    print('>><<'*20)
    n = str(input('Imformação invalida. digite seu sexo [H/M]')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(n))