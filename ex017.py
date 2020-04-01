
import math
# aqui esta sendo importado tudo que existe na biblioteca math
# from math import hypot ...aqui apenas o metodo da hipotenusa esta importado

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))
