maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso#maior peso vai passar ser o peso
        menor = peso#menor peso vai passar ser o peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso lido foi de {}Kg'.format(maior))
print('O moner peso lido foi de {}Kg'.format(menor))

