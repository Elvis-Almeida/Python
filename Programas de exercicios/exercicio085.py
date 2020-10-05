#separar os numeros em uma mesma lista
l = [[],[]]
for c in range(1,8):
    n = int(input(f'Digite o {c}° numero'))
    if n % 2 == 0:
        l[0].insert(0, n)
    else:
        l[1].insert(0, n)
l[0].sort()
l[1].sort()
print(f'Os numeros pares foram {l[0]}')
print(f'Os numeros impares foram {l[1]}')
