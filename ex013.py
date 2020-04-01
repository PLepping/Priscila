# reajuste salarial

salario = float(input("Digite o salario R$:"))
novo = salario + (salario * 15 / 100)

print("O salario de R${:.2f} com 15% de aumento é de R${:.2f}".format(salario, novo))