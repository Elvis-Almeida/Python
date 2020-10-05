#personalizando o ajuda interativa python
from time import sleep
def linha(text):
    '''
    função cria linha personalizadas de acordo com o texto inserido
    :param text: texto a ser inserido
    :return:
    '''
    print('~'*(len(text)+4))
    print(f'  {text}')
    print('~' * (len(text) + 4))

def inhelp(fun):
    '''
    função personalizada do iterative help
    :param fun: comando a ser analizado
    :return:
    '''
    print('\033[1;30;44m')
    help(fun)
    print('\033[m')

#programa principal

while True:
    print('\033[1;30;46m')
    linha('Ajuda Interativa')
    print()
    print('\033[m')
    a = input('\033[mFunção ou biblioteca >>>')
    if a == 'Fim' or a == 'fim' or a == 'FIM':
        break
    print('\033[1;30;45m')
    linha('Analizando...')
    print()
    print('\033[m')
    sleep(1.5)
    inhelp(a)
    sleep(1)
print('\033[1;30;41m')
linha('Programa finalizado')
print()