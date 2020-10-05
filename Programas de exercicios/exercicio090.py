#usando dicionario
d = {}
d['Nome'] = str(input('Nome: ')).strip()
d['Media'] = float(input(f'Media de {d["Nome"]}: '))
if d['Media'] >= 7:
    d['Situação'] = 'Aprovado'
elif 5 <= d['Media'] <= 7:
    d['Situação'] = 'Recuperação'
else:
    d['Situação'] = 'Reprovado'
print('=-' * 20)
for k, v in d.items():
    print(f'   - {k} é igual a {v}')
