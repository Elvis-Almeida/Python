d = dict()
l = list()
soma = 0
while True:
    d['nome'] = str(input('Nome: ')).strip()
    sexo = str(input('Sexo: M/F')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('\033[1;31mErro!\033[m Sexo: M/F ')).strip().upper()
    d['sexo'] = sexo
    d['idade'] = int(input('Idade: '))
    con = str(input('Continuar? S/N ')).strip().upper()
    while con not in 'SN':
        con = str(input('Continuar? S/N ')).strip().upper()
    l.append(d.copy())
    d.clear()
    print('-=' * 20)
    if con in 'N':
        break
print(f'A) Foram cadastradas {len(l)} pessoas')
for c in l:
    soma += c['idade']
print(f'B) A idade media do grupo é {soma/len(l):.2f}')
print('C) As mulheres cadastradas foram:', end=' ')
for d in l:
    if d['sexo'] in 'F':
        print(d['nome'], end=' ')
print()
print('D) Pessoas acima da média:')
for d in l:
    print('   ', end='')
    if d['idade'] > soma/len(l):
        for k, v in d.items():
            print(f'{k} = {v};', end=' ')
    print()
print('<<<< ENCERRADO >>>>')