#calculando IMC
a = float(input('Digite sua Altura em Metros: '))
p = float(input('Digite seu Peso em Kg: '))
imc = p/a**2
print('seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Voçê está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal')
elif 25 <= imc < 30:
    print('Voçê está com sobrepeso')
elif 30 <= imc < 40:
    print('Voçê está com obesidade')
else:
    print('Voçê está com obsidade mórbida')
