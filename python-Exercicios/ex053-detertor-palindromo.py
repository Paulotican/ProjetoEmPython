frase = str(input('Digite uma frase: ')).strip().upper()#strip vai tira os espaços e o upper vai deixa tdas letra em mauscular
palavras = frase.split()#split gera uma lista
junto = ''.join(palavras)#join vai preenche o espaço vacio
#inverso = ''
inverso = junto[::-1]#fatiamento sem usar o FOR
'''for letra in range(len(junto) -1, -1, -1,):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

#print('Você digitou a frase {}'.format(junto))
