from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu: '))
idade = atual - nasc
print('O Atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Atleta mirim')
elif idade <= 14:         #14 > idade >=10:
    print('Atleta INFANTIL')
elif idade <= 19:         #19 > idade >= 15:
    print('Atleta JUNIOR')
elif idade <= 25:         #26 > idade >= 20:
    print('Atleta SÊNIOR')
else:
    print('Atleta MASTER')