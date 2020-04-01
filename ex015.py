# alugueis de carros

dias = int(input("Digite a quantidade de dias: "))
km = float(input("Digite a quantidade de km: "))
diarias = (dias * 60) + (km * 0.15)

print("O total a pagar é de R${:.2f}".format(diarias))
