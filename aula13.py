i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('fimm')

s = 0
for c in range (0, 5):
    n = int(input('Digite um numero: '))
    s += n
print('O somatorio de todos os valores foi {}'.format(s))