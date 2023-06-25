# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira Ex: Digite um número: 6.127 o número tem a parte inteira 6 #
from math import trunc 
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porça inteira é {}.'.format(num, trunc(num)))