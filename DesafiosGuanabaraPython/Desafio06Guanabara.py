# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada. #
valor = int(input('Escreva um número: '));
dobro = valor*2
triplo = valor*3
raiz = valor**(1/2)
print('o dobro do seu número é {}, o triplo é {} e a raiz quadra é {:.3f}'.format(dobro, triplo, raiz))