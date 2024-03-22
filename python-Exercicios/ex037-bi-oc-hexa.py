num = int(input('Digite um número inteiro: '))
print('''Escreva uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECINAL''')
opção = int(input('sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO e igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL e igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HECADECINAL e igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente')
