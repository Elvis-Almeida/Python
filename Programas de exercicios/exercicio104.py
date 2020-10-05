#validação de numero inteiro
def leiaint(tex):
    a = input(tex)
    while not a.isnumeric():
        print('\033[1;31mERRO! Digite um numero inteiro válido\033[m')
        a = input(tex)
    return int(a)


#programa principal
b = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {b}')