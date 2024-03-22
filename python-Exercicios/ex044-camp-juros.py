print('{:=^40}'.format(' Lojas Teste '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTOS
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartâo ''')
opção = int(input('Qual é a opção: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas: '))
    parcela = total / totparc
    print('Sua compra será percalada em {}x R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO INVALIDA de pagamento. Tente novamente')

print('Sua compra de R${:.2f} vai custa R${:.2F} no final'.format(preço, total))
