# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade_carro = float(input('Qual a velocidade do carro? '))
limite_velocidade = 80
acima_limite = (velocidade_carro - limite_velocidade) * 7
if velocidade_carro > limite_velocidade:
    print('Voce foi multado! R${:.2f}'.format(acima_limite))
else :
    print('Tenha um bom dia! Dirija com segurança!')
    