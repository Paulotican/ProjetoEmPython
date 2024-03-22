salário = float(input('Qual é o salário do funcionario? R$'))
if salário <= 1250:
    novo = salário + (salário * 7 / 100)
else:
    novo = salário + (salário * 4.5 / 100)
print('Quem ganhava R${:.2f} passa a ganha R${:.2f} agora.'.format(salário, novo))
