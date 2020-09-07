#caso o system('cls') dê erro mude para system('clear')
import random
from os import system 

lista_de_entrada_de_componentes = [] #lista que recebe a quantidade de cada componente

def lerInt(txt): #para só aceitar entrada de numero
    while True: 
        numero = input(txt)
        if len(numero) == 0:
            numero = 'a' 
        if numero in '1234567890':
            return int(numero)
        else:
            print('\033[1;31mDigite um numero\033[m')

def lerComponentes(lista): #ler a quantidade de cada componente (ladrão, detetive, vítima)
    system('cls') #para limpar o terminal
    print('='*50) #para desenhar uma linha
    for ignora in range(0, lerInt('Digite a quantidade de vítimas: ')): #adiciona a quantidade de Vitima a lista
        lista.append('Vítima')
    print('='*50)
    for ignora in range(0, lerInt('Digite a quantidade de Detetives: ')): #adiciona a quantidade de Detetives a lista
        lista.append('Detetive')
    print('='*50)
    for ignora in range(0, lerInt('Digite a quantidade de Ladrões: ')): #adiciona a quantidade de Ladrão a lista
        lista.append('Ladrão')
    system('cls')
    return lista

def misturarLista(lista): #vai deichar a lista em ordem aleatória
    random.shuffle(lista)
    return lista

def mostrarNaTela(lista): #para mostrar a lista na tela
    for componente in lista:
        system('cls') #para limpar o terminal
        input(f'\033[1;32m{"Pressione Enter":^30}') #para servi como botão
        for ignora in range(0, 6): #para fazer o alinhamento vertical
            print('') #para deixar os espaços em branco
        print(f'\033[1;36m{componente:^30}\033[m')
        for ignora in range(0, 6): #para fazer o alinhamento vertical
            print('') #para deixar os espaços em branco
        input(f'\033[1;32m{"Pressione Enter":^30}') #para servi como botão
    print(f'\033[1;41m{"Você foi o ultimo":^30}\033[m') #esses codigos são para pintar o terminal


lerComponentes(lista_de_entrada_de_componentes)
misturarLista(lista_de_entrada_de_componentes)
mostrarNaTela(lista_de_entrada_de_componentes)

    
    