l = []
o = 0
i = 0
maior = menor = 0
for c in range(0,5):
    n = int(input('Digite seu numero'))
    if o == 0:
        l.append(n)
        o = 1
    if o == 1:
        maior = menor = n
        o = 2
    else:
        if maior < n:
            maior = n
            l.append(n)
            print('Seu numero foi adicionado no final da lista')
        elif menor > n:
            menor = n
            l.insert(0, n)
            print('Seu numero foi adicionado no começo da lista')
        elif maior == n:
            l.insert(l.index(n), n)
        elif menor == n:
            l.insert(l.index(n), n)
        else:
            h = 0
            for y in range(0,len(l)):
                if l[y] > n and h == 0:
                    i = l.index(l[y])
                    print(f'Seu numero foi adicionado na posição {l.index(l[y])}')
                    if l[y-1] != l[y]:
                        h = 1
            l.insert(i, n)
print('=-'*20)
print(f'Sua lista foi {l}')
