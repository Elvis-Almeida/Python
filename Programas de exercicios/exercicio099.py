#analizador de numero maior
from time import sleep


def maior(* l):
    print('-='*20)
    print('Analizando valores...')
    print('Dentre os valores informados:',end=' ')
    ma = 0
    if len(l)>0:
        for c, v in enumerate(l):
            print(v, end=' ', flush=True)
            sleep(0.3)
            if c == 0:
                ma = v
            elif ma < v:
                ma = v
    print(f', São ao todo {len(l)}')
    print(f'o maior valor encontrado foi {ma}')

# programa principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()