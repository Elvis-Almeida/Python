#simulador de caixa eletronico
total = c = c1 = mc = 0
while True:
    print('-=' * 20)
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$'))
    total += preco
    c1 += 1
    if preco > 1000:
        c += 1
    if c1 == 1 or mc > preco:
        mc = preco
        n = nome
    print('-=' * 20)
    para = str(input('Finalizar compra? [S/N]')).strip().upper()[0]
    while para not in 'NS':
        para = str(input('Finalizar compra? [S/N]')).strip().upper()[0]
    if para == 'S':
        break
print('-=' * 20)
print(f'\033[30mO total de sua compra é R${total:.2f}')
print(f'Há {c} produtos com mais de R$1000.00')
print(f'O produto mais barato foi {n} valendo {mc:.2f}')