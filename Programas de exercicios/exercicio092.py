import datetime
d = {}
d['Nome'] = str(input('Nome: ')).strip()
d['Ano de nascimento'] = int(input('Ano de nascimento: '))
d['Idade'] = datetime.date.today().year - d['Ano de nascimento']
ca = int(input('Carteira de trabalho (0 não tem): '))
if ca != 0:
    d['ctps'] = ca
    d['Contratação'] = int(input('Ano de comtratação: '))
    d['Salario'] = int(input('Salário: '))
    d['Aposentadoria'] = (d['Contratação'] + 35) - d['Ano de nascimento']
print('--'*20)
for k, v in d.items():
    print(f'     -{k} tem o valor de {v}')
