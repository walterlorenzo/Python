# Faça um programa que leia três números e mostre qual é o maior e qual é a menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número: '))
n3 = int(input('Digite um terceiro número: '))
# Verificando quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))

