#contador de multa sendo multado apartir de 80Km/h e 7 reais por km a mais
print(':)' * 5)
print('multrometro')
print(':)' * 5)
n = int(input('digite sua velocidade: '))
if n>80:
    m = 7 * (n-80)
    print('Voçê foi multado. Sua multa é R${:.2f}'.format(m))
else:
    print('voçê não foi multado. Tenha um Bom Dia!')