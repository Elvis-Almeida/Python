#lendo boletin com o que for pedido
l = []
r = []
while True:
    r.append(input('Nome do aluno: '))
    r.append(float(input('Nota 1: ')))
    r.append(float(input('Nota 2: ')))
    l.append(r[:])
    r.clear()
    continua = str(input('Deseja adicionar mais alunos? S/N ')).strip().lower()
    if continua[0] in 'n':
        break
print(f'{" Media dos alunos ":=^40}')
print('    Nº    Aluno               Media')
for v, b in enumerate(l):
    print(f'{v:^10}',end='')
    print(f'{b[0]:<10}', end='     ')
    print(f'{(b[1]+b[2])/2:8.1f}')
while True:
    print()
    a = int(input('Qual aluno deseja ver as notas? (-1 para parar)'))
    if a < 0:
        break
    if a < len(l):
        print('=' * 40)
        print('           ', end='')
        for w in l[a]:
            print(w,end='  ')
        print()
        print('=' * 40)
    else:
        a = int(input('Qual aluno deseja ver as notas? (-1 para parar)'))
print('<<<<< Boletin finalizado >>>>>')