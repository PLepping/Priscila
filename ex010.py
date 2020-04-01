#conversor de moedas

n = float(input("Digite um valor em R$: "))
dolar = n /3.74

print("Com o valor de R${:.2f} vc pode comprar US${:.2f}".format(n, dolar))