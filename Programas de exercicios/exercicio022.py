#informacões sobre o nome
nome = str(input('digite seu nome')
print("seu nome com todas as letras maiusculas:{}".format(nome.upper().strip()))

print('seu nome com todas as letras minusculas:{}'.format(nome.lower().strip()))

q = int(len(nome.strip()))
#ou
#r = nome.count(' ')
#print(q-r)
di = nome.split()
a = int(len(di))
print('seu nome tem {} letras'.format(q-(a-1)))

g = di[0]
print('seu primeiro nome tem {} letras'.format(len(g)))


