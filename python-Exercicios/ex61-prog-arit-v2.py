primeiro = int(input('Primeiro terno: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 11:
    print('{} '.format(termo), end='-> ')
    #termo = termo + razão
    termo += razão
    cont += 1
print('Acabou')