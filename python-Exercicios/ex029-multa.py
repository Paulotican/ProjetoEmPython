velocidade = float(input('Qual é a velocidade ataul do carro: '))
if velocidade >= 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80KM/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de {:.2f}'.format(multa))
print('tenha uma bom dia! Dirija com segurança')