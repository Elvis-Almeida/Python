#calculando o preço da viagen
p = int(input('digite a distancia em km de sua viajem: '))
if p > 200:
    print('o preço de sua viagem será de R${:.2f}'.format(0.45*p))
else:
    print('o preço de sua viagem será de R${:.2f}'.format(0.5*p))