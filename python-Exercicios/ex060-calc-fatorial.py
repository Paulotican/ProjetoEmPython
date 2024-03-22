#from math import factorial
num = int(input('Digite um número para calcular seu Fatorial: '))
con = num
fac = 1
print('Calculando {}! = '.format(num), end=' ')
while con > 0:
    print('{}'.format(con), end=' ')
    print(' x ' if con > 1 else ' = ', end=' ')
    fac *= con#fac = fac * con
    con -= 1
#fac = factorial(num)
print('{}'.format(fac))
