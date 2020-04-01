tempo = int(input('Quantos anos tem seu carro: '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')

#print('carro novo'if tempo <=3 else 'carro velho') maneira simplificada

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua media foi {:.1f}'.format(m))

if m >= 6.0:
    print("Sua media foi boaaaaaaaaaaa")
else:
    print("Estude maisssssssss")