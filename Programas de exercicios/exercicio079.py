#adicione numeros diferentes
l = []
while True:
    p = int(input('Digite um numero: '))
    if p in l:
        print('Esse numero não pode ser adicionado, pois já esta em sua lista')
    else:
        print('Numero adicionado com sucesso!')
        l.append(p)
    q = str(input('Quer continuar? S/N')).strip().upper()
    while q not in 'SN':
        q = str(input('Quer continuar? S/N')).strip().upper()
    if q == 'N':
        break
print(f'Sua lista foi {sorted(l)}')
