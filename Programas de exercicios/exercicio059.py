#operação com menu
from time import sleep
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite segundo numero: '))
para = False
while not para:
    print(''' Qual operação deseja fazer
    [1] Somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa ''')
    print('>>>>'*10)
    op = int(input('Qual operação dejasa usar:'))
    if op == 1:
        soma = n1 + n2
        print('Sua soma de {} + {} é {}'.format(n1,n2,soma))
        print('>>>>'*10)
        sleep(2)
    elif op == 2:
        multiplicar = n1 * n2
        print('Sua multipliação de {} X {} é {}'.format(n1,n2,multiplicar))
        print('>>>>'* 10)
        sleep(2)
    elif op == 3:
        if n1 > n2:
            print('O numero maior é {}'.format(n1))
        elif n2 > n1:
            print('O numero maior é {}'.format(n2))
        elif n2 == n1:
            print('{} é igual a {}'.format(n1,n2))
        print('>>>>'*10)
        sleep(2)
    elif op == 4:
        print('Informe seus novos numeros')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite seu segundo valor: '))
    elif op == 5:
        para = True
        print('>>>>'*10)
    else:
        print('\033[1;31mOpção invalida. Tente novamente!\033[m')
        print('>>>>'*10)
        sleep(2)
print('\033[1;31mPrograma encerrado')