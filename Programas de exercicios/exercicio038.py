#dizer qual deles é o maior ou menor
n1 = float(input('digite o 1º numero'))
n2 = float(input('digite o 2º numero'))
if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os valores são iguais!')