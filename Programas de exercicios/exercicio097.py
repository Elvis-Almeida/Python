#texto adaptavel
def escreva(a):
    t = len(a)+4
    print('\033[1m~'*(t))
    print(f'  {a}')
    print('~' * (t))


escreva(str(input('Digite sua frase!')))