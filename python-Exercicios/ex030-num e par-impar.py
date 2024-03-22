número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é um número PAR'.format(número))
else:
    print('O número {} é um número IMPAR'.format(número))
