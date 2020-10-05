def votação(idade):
    import datetime
    '''
    Diz se a pessoa pode ou não votar
    :param idade: ano de nascimento
    :return: retorna situação de votação
    '''
    ano = datetime.date.today().year
    si = ano - idade
    if si < 16:
        r = 'Não Vota'
    elif 16 <= si <=17 or si > 65:
        r = 'Voto opicional'
    elif 17 < si < 65:
        r = 'Voto obrigatorio'
    return f'Com {si} anos, {r}'


#programa principal
a = votação(int(input('Ano de nascimento')))
print(a)