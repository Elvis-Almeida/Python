#tabuada com for
print('{:=^20}'.format('tabuada'))
n = int(input('digite um numero:'))
for c in range(1, 11):
    r = n * c
    print('{} X {} = {}'.format(n, c, r))