#saber se uma expressao matematica esta com os parenteses corretos
f1 = []
k = 0
n = str(input('digite sua expressão'))
for c in range(0, len(n)):
    if n[c] == ')':#procurando apenas os parenteses
        f1.append(n[c])
    if n[c] == '(':
        f1.append(n[c])
    if f1[c] == '(':#analisando se estão de forma correta
        k += 1
    elif f1[c] == ')':
        k -= 1
    if k < 0:#dando o resultado
        break
if k > 0 or k < 0:
    print('Sua expressão está errada')
else:
    print('Sua expressão está correta')




