from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    #print('Essa pessoa tem {} anos'.format(idade))
    if idade >= 21:
        totmaior += 1
    else:
        totmenor+= 1
print('Ao todos tivemos {} pessoas maiores de idades'.format(totmaior))
print('E também tivemos {} pessoas menores de idades'.format(totmenor))