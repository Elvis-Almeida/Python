#se uma cidade tem ou nao no nome santo
n = input('digite o nome de uma cidade: ')
p = n.upper().strip().split()
q = p[0]
r = str('SANTO' in p)
print('tem santos no primeiro nome de sua cidade? {}'.format(r))

#ou
nome = str(input("digite o nome de uma cidade")).strip()
print(nome[:5].upper() == 'SANTO')