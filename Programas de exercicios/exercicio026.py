nome = str(input('digite uma frase: ')).strip().lower()
print('sua frase tem {} A'.format(nome.count('a')))
print('o ultimo A aparece na posição {}'.format(nome.rfind("a")+1))
print('o primeiro A aparece na posição {}'.format(nome.find('a')+1))
