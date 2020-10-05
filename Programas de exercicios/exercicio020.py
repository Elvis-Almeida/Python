#sortear a ordem dos alunos
import random
n1 = input('aluno 1: ')
n2 = input('aluno 2: ')
n3 = input('aluno 3: ')
n4 = input('aluno 4: ')
l = [n1, n2, n3, n4]
random.shuffle(l)
print('a ordem é {}'.format(l))