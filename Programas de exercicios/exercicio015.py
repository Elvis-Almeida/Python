#aluguel do carro sendo 60 reais o dia e 0.15 o km rodado
print('calcule quanto fica o aluguel do carro')
dias = int(input('digite o numero de dias usado: '))
km = float(input('digite quantos km voçê rodou: '))
a = (dias*60)+(km*0.15)
print ('o valor do seu aluguel é de R${:.2f}'.format(a))