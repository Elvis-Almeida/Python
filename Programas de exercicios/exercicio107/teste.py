from Exercicios.exercicio107 import moeda
p = int(input('digite um valor: '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'10% aumetado é {moeda.aumentar(p, 10)}')
print(f'o dobro de {p} é {moeda.dobro(p)}')
print(f'5% a menos é {moeda.diminuir(p, 5)}')
