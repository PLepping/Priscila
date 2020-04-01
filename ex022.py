"""Nome com todas as maiusculas e minusculas,qtas letras ao todo sem os espacos e qtas letras tem o 
primeiro nome"""

nome = str(input('Digite seu nome completo: ')).strip() # vai eliminar os espacos, posso usar-la direto
print ('Analisando seu nome...')
print('Seu nome em maiusculas e {}'.format(nome.upper()))
print('Seu nome em minusculas e {}'.format(nome.lower()))
print('Seu tem ao todo tantas {} letras'.format(len(nome) - nome.count(' '))) #conta do total de letras menos os espacos entre elas
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()# split coloca todas palavras em lista
print('Seu primeiro nome e {} e tem {} letras'.format(separa[0], len(separa[0])))
