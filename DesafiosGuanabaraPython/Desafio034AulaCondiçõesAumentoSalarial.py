# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule aumento de 10%.
# Para inferiores ou iguais, o aumento é de 15%.

salario = float(input('Quanto é seu salário? '))
aumento_15 = salario + ((salario / 100) * 15)
aumento_10 = salario + ((salario / 100) * 10)
if salario <= 1250:
    print('Parabéns, você recebeu um aumento de 15%, seu salário agora é R${}'.format(aumento_15))
else:
    print('Você recebeu um aumento de 10%, seu salário agora é R${:,=.}'.format(aumento_10))
