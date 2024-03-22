from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=-' *8)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-' *8)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE') #jogou PEDRA
    elif jogador == 1:
        print('JOGADOR VENCE')# jogou PAPEL
    elif jogador == 2:
        print('COMPUTADOR VENCE')#j ogou TESOURA
    else:
        print('JOGADA INVALIDA')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')#jogou PEDRA
    elif jogador == 1:
        print('EMPATE')# jogou PAPEL
    elif jogador == 2:
        print('JOGADOR VENCE')#jogou TESOURA
    else:
        print('JOGADA INVALIDA')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')#jogou PEDRA
    elif jogador == 1:
        print('COMPUTADOR VENCE')# jogou PAPEL
    elif jogador == 2:
        print('EMPATE')#j ogou TESOURA
    else:
        print('JOGADA INVALIDA')

