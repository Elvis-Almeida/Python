n1 = (str(input(f'Digite o 1º numero: ')))
n2 = (str(input(f'Digite o 2º numero: ')))
n3 = (str(input(f'Digite o 3º numero: ')))
n4 = (str(input(f'Digite o 4º numero: ')))
n = (n1,n2,n3,n4)
print(f'Você digitou {n}')
if n.count('9') > 0:
    print(f'há {n.count("9")} nove(s)')
else:
    print('Não há nenhum nove')
if n.count('3') > 0:
    print(f'O primeiro três apareçe na {n.index("3")+1}ª posição ')
else:
    print('Não há nenhum 3')
p = 0
u = 0
print('Os numeros pares são:', end=' ')
for c in n:
    if c == p:
        u += 1
        p = c
    elif int(c) % 2 == 0:
        print(c,end=' ')
        u += 1
        p = c
if u == 0:
    print('Nenhum')