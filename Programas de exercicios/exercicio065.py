para = 'S'
c = s = maior = menor = 0
while para != 'N':
    n = int(input('Digite um valor: '))
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        elif menor > n:
            menor = n
    s += n
    para = str(input('Quer continuar?[S/N] ')).strip().upper()
media = s/c
print('A media dos {} numeros digitados é {:.2f}'.format(c,media))
print('O maior foi {} e o menor foi {}'.format(maior,menor))