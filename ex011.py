# pintando parede

larg = float(input("Digite a largura:"))
alt = float(input("Digite o comprimento:"))
area = larg * alt

print("Sua parede tem {} x {} e sua área é de {}m².".format(larg, alt, area))

tinta = area / 2
print("Para pinta essa parede vc precisará de de {}l de tinta".format(tinta))
