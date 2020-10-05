#a soma de numeros inpares multiplos de 3 entre 1 e 500
s = 0
w = 0
for c in range(3, 500, 3):
    if c%2 == 1:
        s += c
        w += 1
print('a soma de {} numeros inpares multiplos de 3 entre 1 e 500 é {}'.format(w,s))