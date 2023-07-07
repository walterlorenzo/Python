# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

km_viagem = int(input('Qual a distância da viagem? '))
if km_viagem <= 200:
    preco_viagem = km_viagem * 0.50
    print('O preço da passagem é R${:.2f}'.format(preco_viagem))
if km_viagem > 200:
    preco_viagem = km_viagem * 0.45
    print('O preço da passagem é R${:.2f}'.format(preco_viagem))
