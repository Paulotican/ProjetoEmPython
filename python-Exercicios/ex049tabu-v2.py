from time import sleep
num = int(input('Digite um número para sua tabuada: '))
for n in range(0, 11):
    print('{} x {:2} = {}'.format(num, n, num*n))
    sleep(0.4)

# print('=' * 12)