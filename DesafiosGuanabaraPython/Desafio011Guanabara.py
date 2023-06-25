# Faça um programa que leia a largura e a altura de uma parada em metros, Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m². #

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parde: '))
área = larg * alt
print('Sua parede tem a dimensão {}x{} e sua área é de {}m².'.format(larg, alt, área))
tinta = área / 2
print('Para pitnar essa parede, você precisa de {}l de tinta.'.format(tinta)) 