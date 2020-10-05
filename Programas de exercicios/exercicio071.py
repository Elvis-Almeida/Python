#simulador de caixa eletronico
'''q = int(input('Quanto quer sacar? R$'))
n50 = q // 50
n20 = (q - (n50 * 50)) // 20
n10 = (q - ((n50 * 50)+(n20 * 20))) // 10
n1 = (q - ((n50 * 50)+(n20 * 20)+(n10 * 10))) // 1
print('Voçê vai receber')
if n50 > 0:
    print(f'{n50} notas de R$50.00')
if n20 > 0:
    print(f'{n20} notas de R$20.00')
if n10 > 0:
    print(f'{n10} notas de R$10.00')
if n1 > 0:
    print(f'{n1} moedas de R$1.00')'''
# Ou
q = int(input('Quanto quer sacar? R$'))
total = q
c = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        c += 1
    else:
        if c > 0:
            print(f'Total de {c} de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break
        c = 0