'''criar uma função que vai receber algumas cidades(5)
vão organizar em ordem alfabética'''

cidades = []

for x in range(5):
    nomes = input(f'Digite a {x+1}° cidade: ')
    cidades.append(nomes)

alfa = sorted(cidades)
print(cidades)
print(alfa)