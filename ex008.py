#conversor de medidas

medida = float(input("Digite uma distancia em metros: "))
cm = medida * 100
mm = medida * 1000

print("A distância de{}m corresponde a {:.0f}cm e {:.0f}mm".format(medida, cm, mm))