#valor de desconto ou de juros
print('\033[1;36m{:=^40}'.format(' Lojas ERA '))
print(' ')
valor = float(input('\033[1;34mDigite o valor da compra R$'))
print('''\033[1;33mFormas de pagamento:
\033[1;30m1) para à vista Dinheiro/Cheque
2) para à vista cartão
3) para 2X no cartão
4) para 3X ou mais no cartão''')
pagamento = int(input('\033[1;34mDigite a Forma de pagamento: \033[1;34m'))
if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
    if pagamento == 1:
        final = valor - (valor*10/100)
        texto = 'com desconto'
        print('Seu valor final será de R${:.2f} {}'.format(final, texto))
    elif pagamento == 2:
        final = valor - (valor*5/100)
        texto = 'com desconto'
        print('Seu valor final será de R${:.2f} {}'.format(final, texto))
    elif pagamento == 3:
        final = valor
        texto = ''
        print('Suas parcelas serão de R${:.2f}'.format(final/2))
        print('Seu valor final será de R${:.2f} {}'.format(final, texto))
    elif pagamento == 4:
        vezes = int(input('Quantas vezes quer dividir?\033[1;33m '))
        if vezes<3:
            print('\033[1;31mEscolha mais vezes para dividir! TENTE NOVAMENTE')
        else:
            final = valor + (valor*20/100)
            mes = final/vezes
            print('Voçê pagarar {} por mês com 20% de juros'.format(mes))
            texto = 'com juros'
            print('Seu valor final será de R${:.2f} {}'.format(final,texto))
else:
    print('\033[1;31mForma de pagamento INVALIDA')
