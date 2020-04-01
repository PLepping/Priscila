nome = str(input("Qual seu nome: "))

if nome == "Priscila":
    print("Que nome bonito")
elif nome == "Pedro" or nome == "Paula" or nome == 'Maria':
    print('Seu nome e popular no Brasil!')
else:
    print("Nome normal")
print("Tenha um bom dia, {} !!!".format(nome))