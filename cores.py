print("\033[1;31;43mOla MUNDO\033[m")
print("\033[4;30;45mOLA MUNDOOOO\033[m")
print("\033[7;30mOLA MUNDO\033[m")
print("\033[7;31;47mOLA MUNDO\033[m")

a = 3
b = 5
print("Os valores sao \033[32m{}\033[m e \033[31m{}\033[m!!!".format(a,b))
nome = "Priscila"
print("Ola!! Muito prazer em te conhecer, {}{}{}".format("\033[4;34m",nome, "\033[m"))

cores = {"limpa":"\033[m",
         "azul":"\033[34m",
         "amarelo":"\033[33m",
         "pretobranco":"\033[7;30m"}
print("Ola {}{}{}".format(cores["pretobranco"],nome,cores["limpa"]))

num = 4.999
print(int(num))

a = 3
b = 5
if a>b:
    print("x")
else:
    print("Y")
    print("W")
print("Z")

num = '7'
res = int(num) / 2
print(type(res))

valor = '153'
parte = "5"
valor += parte
print(valor.isnumeric())

from random import randint
num = randint(1, 6)
res = num // 2
print(res)

texto = 'Tres Pratos de Trigo para Tigres Tristes'
total = texto.upper().count(texto[0])
print(total)

a = 4
b = 3
c = 2
d = a + b * c
e = d % c + 1
print("{} e {}".format(d, e))

frase = 'Curso em Video de Python'
separado = frase.split()
palavra = separado[2]
letra = palavra[3]
print(letra.upper())