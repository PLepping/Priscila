# leia  os nomes e mostre a ordem sorteada

from random import shuffle

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome:'))
lista = [n1, n2, n3]
shuffle(lista)

print('A ordem de apresentacao sera ')
print(lista)