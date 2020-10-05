#10 termos de uma PA
r = int(input('Digite a razão de sua PA'))
i = int(input('Digite o numero snde começarar sua PA'))
print('sua PA é...')
for c in range(i, i+10*r, r):
    print('\033[1;30m',c, end=' ')