#calcular a situção da sala
def notas(*notas, sit=False):
    '''
    função mostra a situação das notas informadas
    :param notas: notas dos alunos
    :param sit: mostra a situação das notas(False por padrão
    :return: situação das notas
    '''
    sitsala = {}
    sitsala['Total'] = len(notas)
    v = 0
    s = 0
    for c in notas:
        s += c
        if v == 0:
            M = c
            m = c
            v +=1
        else:
            if M < c:
                M = c
            if m > c:
                m = c
    sitsala['Maior'] = M
    sitsala['Menor'] = m
    media = s/len(notas)
    sitsala['Media'] = media
    if sit:
        if media < 4:
            sitsala['situação'] = 'Ruin'
        elif media >= 7:
            sitsala['situação'] = 'Boa'
        else:
            sitsala['situação'] = 'Regular'
    return sitsala

#programa principal
a = notas(7,7,7,7,7,4,5,3,2,3,5,6,8,9,8,7,8,6,4,2,24)
print(a)