n = str(input('Digite se nome completo: ')).strip()#strip eliminar os espaço
nome = n.split()#split vai divite em lista
print('Muito prazer em ter conhever!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))#len vai conta qndo posição
