# Escreva um código que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
num = random.randint(0, 5)
numero_escolhido = int(input('Escolha um número entre 0 e 5: '))
if numero_escolhido == num:
    print('Voce venceu!')
else:
    print('Voce perdeu!')
