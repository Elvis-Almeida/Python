#somando até digitar 1000
c = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 1000:
        break
    c += 1
    s += n
print(f'Seus {c} numeros somados são {s}')
