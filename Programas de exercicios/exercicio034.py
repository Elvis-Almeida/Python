#calculo de aumento de salario
s = float(input('digite seu salario'))
if s > 1250:
    a = (s*10/100)+s
    p = 10
else:
    a = (s*15/100)+s
    p = 15
print('seu salario com {}% de aumento fica R${:.2f}'.format(p,a))