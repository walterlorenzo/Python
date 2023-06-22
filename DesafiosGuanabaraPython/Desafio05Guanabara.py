# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor #

numero_inteiro = int(input('Digite um número inteiro: '));
numero_antecessor = numero_inteiro - 1
numero_sucessor = numero_inteiro + 1
print('Numéro antecessor é {} e o numéro sucessor é {}'.format(numero_antecessor, numero_sucessor))