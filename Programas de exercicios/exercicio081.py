l = []
r = []
while True:
    l.append(int(input('Digite um numero')))
    p = str(input('Quer continuar? S/N')).strip().upper()
    while p not in 'NS':
        p = str(input('Quer continuar? S/N')).strip().upper()
    if p == 'N':
        break
print('=-' * 30)
print(f'Foram digitados {len(l)} numeros')
l.sort(reverse=True)
print(f'A lista em ordem decrescente é {l}')
if 5 in l:
    tex = 'O numero 5 faz parte de sua lista'
else:
    tex = 'O numero 5 não foi encontrado em sua lista'
print(tex)


