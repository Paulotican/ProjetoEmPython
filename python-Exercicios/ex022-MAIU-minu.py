nome = str(input('Digite seu nome: ')).strip()#tira os espaço do inicio e fim da frase
print('Analisando seu nome')
print('Seu nome maiúsculo é {}'.format(nome.upper()))#vai deixa as letras q esta em munúcula para maiúculas
print('Seu nome minúculo é {}'.format(nome.lower()))#vai deixa as letras q esta em maiúculas para minúcula
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))#vai eliminar os espaços no meio da frase
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
