#ficha do jogador
def ficha(nome='<desconhecido>', gols=0):
    '''
    apresenta uma ficha com os dados cadastrados
    :param nome: nome do jogador
    :param gols: quantidade de gols macados pelo jogador
    :return: ficha com os dados do jogador
    '''
    if gols not in '1234567890':
        gols = '0'
    if len(nome) <= 0:
        nome='<desconhecido>'
    if len(gols) <= 0:
        gols = 0
    return f'O Jogador {nome}, Fez {gols} gol(s)'


#programa principal
b = str(input('Jogador: ')).strip()
c = input('gols macados: ')
a = ficha(b, c)
print(a)