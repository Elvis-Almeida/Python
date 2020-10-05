#se um numero é ou nao numero primo
n = int(input('digite um numero'))
t = 'é PRIMO'
for c in range(2, n):
    if n % c == 0:
        t = 'não é PRIMO'
if n == 1:
    t = 'nao é PRIMO'
print('\033[1;30mSeu numero {} {}'.format(n,t))
