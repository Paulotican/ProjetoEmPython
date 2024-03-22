primeiro = int(input('Primeiro terno: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:# != diferente de
    total = total + mais
    #total += mais
    while cont <= total:
        print('{} '.format(termo), end='-> ')
        #termo = termo + razão
        termo += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer modtrsar mais: '))
print('Progressão finalizada com {} termos mostrados'.format(total))