produtos = ('Caderno', 25.60, 'Lápis', 0.50, 'Caneta', 1.50, 'Borracha', 2.40,
            'Tesoura', 3.50, 'Cola', 2.50, 'Corretivo', 4.20,
            'Apontador', 1.50, 'Bolsa', 135.90)
print('\033[1;36m-=-' * 4, 'Mercado em Python', '-=-' * 4)
for c in range(0, len(produtos), 2):
    print('\033[1;30m{:.<35} \033[1;34mR${:.2f}'.format(produtos[c], produtos[c + 1]))
