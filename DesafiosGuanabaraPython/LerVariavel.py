#Ler váriavel#

a = input("Digite algo: ")
print("o tipo primitivo desse valor é ", type(a))
print("Só tem espaços?", a.isspace())
print("É um número?", a.isnumeric())
print("É alfabético?", a.isalpha())
print("É alfanúmerico?", a.isalnum())
print("Está em maiúsculas?", a.isupper())
print("Está em minúsculas?", a.islower())
print("Está capitalizada?", a.istitle())