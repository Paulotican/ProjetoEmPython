sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]#strip elimina o espaço, upper deixa tdo em maiuculos e o [0] pega a primeira letra
while sexo not in 'MnFf':
    sexo = str(input('Dados inalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))
