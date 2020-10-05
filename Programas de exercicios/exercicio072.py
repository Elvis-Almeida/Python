nomes = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um numero de 0 a 20: '))
    while -1 < n > 21:
        n = int(input('Numero não aceito. Digite um numero entre 0 e 20'))
    print(f'O numero escolhido foi {nomes[n]}')
    para = str(input('Deseja continuar? S/N')).strip().upper()[0]

    if para == 'N':
        break
