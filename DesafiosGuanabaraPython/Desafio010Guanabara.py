# Cria um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar Considere US$1.00 = R$4.74 #

real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = real / 4.74
print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))