#encontrar o primeiro e o ultimo nome
n = str(input('digite seu nome: ')).strip()
a = n.split()
b = int(len(a))
print('Olá {}'.format(n))
print('seu primeiro nome é {}'.format(a[0]))
print('seu ultimo nome é {}'.format(a[b-1]))
