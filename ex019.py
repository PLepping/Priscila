# sorteio de nomes

from random import choice

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))

lista = [n1, n2, n3]
escolhido = choice(lista)
print('O escolhido foi {}'.format(escolhido))