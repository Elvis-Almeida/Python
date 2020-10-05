t = str(input('Digite um texto')).strip().split()
t = ''.join(t).upper()
l = int(len(t))
v = int(l/2)+1
a = 0
b = -1
f = 'é um Polindeto'
for c in range(0, v):
    a += 1
    b += 1
    i = 0+b
    y = l-a
    if t[i] != t[y]:
        f = 'nâo é Polindeto'
print(f)