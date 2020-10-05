nomes = ('CADERNO', 'BOLSA', 'LIVRO', 'BANHEIR0',
         'LIXO', 'VICTOR', 'DEBORA', 'CASA', 'PROGRAMADOR',
         'CURSO', 'GUANABARA', 'PAVILHAO')
for c in nomes:
    print(f'\n\033[mNo nome \033[30m{c}\033[m temos as vogais:\033[34m', end=' ')
    for r in range(0,len(c)):
        h = len(c)
        if c[r] in 'AEIOU':
            print(c[r],end='')
            print(end=' ')