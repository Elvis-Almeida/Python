#para saber se o numero é impar ou par
n = int(input('digite um numero: '))
if n/2 == n//2:
    print('Seu numero é par')
else:
    print('seu numero é impar')

#ou
q = n % 2 #para saber o resto da divisão
if q == 0:
    print('Seu numero é PAR')
else:
    print('seu numero é IMPAR') #se o resto da divisão por 2 é 1, é por que ele é Impar




