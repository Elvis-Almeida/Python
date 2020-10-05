import random #sortear um aluno
n1 = input('nome do aluno 1: ')
n2 = input('nome do aluno 2: ')
n3 = input('nome do aluno 3: ')
n4 = input('nome do aluno 5: ')
l = [n1,n2,n3,n4]
print('o aluno sorteado foi {}'.format(random.choice(l)))
random.randint(0,100)