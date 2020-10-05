#sequencia de fibonacci
n = int(input('Digite um valor: '))
f1 = 0
f2 = 1
f3 = 1
c = n
s = f1, f2, f3
while c > 0:
    f1 = f2 + f3
    f2 = f3 + f1
    f3 = f2 + f1
    s += f1, f2, f3
    c -= 1
print(s[:n])
# OU
'''n = int(input('quantos numeros deseja ver da seguencia: '))
t1 = 0
t2 = 1
t3 = t1 + t2
print('{} >>> {}'.format(t1, t2), end=' >>> ')
c = n
while c > 2:
    print('{}'.format(t3), end=' >>> ')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    c -= 1
print(' FIM')'''