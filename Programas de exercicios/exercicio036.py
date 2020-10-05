#analizador de enprestimo
print('\033[33m^^'*13)
print('\033[1;34mAnalizador de Enpréstimo')
print('\033[33m^^\033[m'*13)
p = float(input('digite o valor do Imovel: '))
s = float(input('digite o valor do seu salario: '))
m = int(input('em quantos anos quer pagar? '))
if (p/(m*12)) > ((30*s)/100):
    print('\033[1;31mSeu enprestimo NÃO foi ACEITO!')
elif (p/(m*12)) < ((30*s)/100):
    print('\033[1;34mSeu enprestimo foi ACEITO!')
