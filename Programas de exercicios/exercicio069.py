#leitor de dados
c = ci = ch = cm = 0
while True:
    c += 1
    print('-=' * 10)
    print(f'     {c}ª pessoa')
    print('-=' * 10)
    idade = int(input('idade: '))
    sexo = str(input('Sexo: [M/F]'))
    while sexo[0] not in 'MmFf':
        sexo = str(input('Sexo: [M/F]'))
    if idade > 18:
        ci += 1
    if sexo[0] in 'Mm':
        ch += 1
    if sexo in 'Ff' and idade < 20:
        cm += 1
    para = str(input('Deseja comtinuar? [S/N]'))
    while para not in 'SsNn':
        para = str(input('Deseja continuar? [S/N]'))
    if para[0] in 'Nn':
        break
print('-=' * 30)
print(f'Há {ci} pessoas com mais de 18 anos')
print(f'Foram cadastrado {ch} Homens')
print(f'Há {cm} mulheres com menos de 20 anos')