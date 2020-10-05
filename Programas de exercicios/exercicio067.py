n = int(input('De qual numero voçê quer ver a tabuada: '))
while True:
    for c in range(1 ,11):
        print(f'{n} X {c} = {n * c}')
    n = int(input('De qual numero voçê quer ver a tabuada? '))
    if n < 0:
        break
print('\033[31mTabuada encerrada!')
