#dividindo em outras listas
l1 = []
l2 = []
l3 = []
while True:
    l1.append(int(input('Digite um numero')))
    continuar = str(input('Deseja continuar? S/N')).strip().upper()
    while continuar not in 'SsNn':
        continuar = str(input('Dejesa continuar? S/N')).strip().upper()
    if continuar == 'N':
        break
for c in l1:
    if c % 2 == 0:
        l2.append(c)
    else:
        l3.append(c)
print('=-'*30)
print(f'''sua lista foi {l1}
seus numeros pares são {l2}
seus numeros impares são {l3}''')