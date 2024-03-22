salario = float(input('Qual e o Salario do funcionario: '))
almen = float(input('almento em por cento: '))
novo_sal = salario + (salario * almen / 100)
#novo_sal = salario + (salario * 15 / 100)


#print('O funcionário que ganhava R% {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}'.format(salario, novo_sal))
print('O funcionário que ganhava R% {:.2f}, com o aumento, passa a receber R$ {:.2f}'.format(salario, novo_sal))