from random import randint
from time import sleep
computador = randint(0, 5)#sotear o número
print('-=-' *21)
print('Vou pensar em um número entre 0 e 5. Tenta adivinhar... ')
print('-=-' *21)
jogador = int(input('Em que número eu pensei? '))#Jogador tenta adidinha
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABENS! Você vencer!')
else:
    print('GANHEI Eu pensei no número {} e não no {}'.format(computador, jogador))


