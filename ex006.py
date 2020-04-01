#mostrar dobro, triplo e raiz quadrada

n = int(input("Digite um número: "))
d = n * 2
t = n * 3
r = n ** (1/2)

print("O dobro de {} de vale {}.".format(n, d)) # (n*2)
print("O triplo de {} de vale {}. \nA raiz quadrada de {} é igual a {:.2f}.".format(n, t, n, r)) #(n, (n*3), n, (n**(1/2))