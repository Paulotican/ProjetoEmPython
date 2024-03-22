peso = float(input('Digite seu peso? (Kg) '))
altura = float(input('Digite sua autura? (m) '))

imc = peso / (altura ** 2)

print("seu imc é de {:.2f}".format(imc))
if imc < 18.5:
    print('Você esta abaixo no peso normal')
elif 18.5 <= imc < 25: # >= 18.5 and < 24.9
    print('Você esta no peso ideal')
elif 25 <= imc < 30: # >= 25 and < 29.9
    print('Você esta com sobrepeso')
elif 30 <= imc < 40: # >= 30 and < 39.9
    print('Você esta com Obecidade')
else:
    print('Você esta com Obecidade móbida')
