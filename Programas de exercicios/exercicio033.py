#dizer dentre 3 numeros qual é o maior
print('^^' * 28)
print("digite 3 numeros para saber qual deles é maior e menor")
print('^^' * 28)
n1 = float(input('numero 1: '))
n2 = float(input('numero 2: '))
n3 = float(input('numero 3: '))
#para saber o maior numero
if n1 > n2 and n1 > n3:
    a = n1
if n2 > n1 and n2 > n3:
    a = n2
if n3 > n1 and n3 > n2:
    a = n3
#para saber o menor numero
if n1 < n2 and n1 < n3:
    b = n1
if n2 < n1 and n2 < n3:
    b = n2
if n3 < n1 and n3 < n2:
    b = n3
print('o menor numero digitado foi {}'.format(b))
print('O maior numero digitado foi {}'.format(a))
#ou
'''maior = n1
if n2>n1 and n2>n3
    maior = n2
if n3>n2 and n3>n1
    maior = n3
    
    
menor = n1
if n2<n1 and n2<n3
    menor = n2
if n3<n2 and n3<n1
    menor = n3
print(menor)
print(maior)'''