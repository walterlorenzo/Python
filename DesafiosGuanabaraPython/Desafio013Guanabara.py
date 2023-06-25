# Faça um algoritmo que leia o salário de um funcionário e mostra seu novo salário, com 15% de aumento.

salário = float(input('Qual o salário do funcionário? R$'))
aumento = salário + (salário * 15 / 100)
print('O salário do funcionário de R${:.2f}, passou por um aumento e atualmente é de R${:.2f}.'.format(salário, aumento))
