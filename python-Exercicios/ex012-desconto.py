preço = float(input('Qual e o valor do produto: '))
novo = preço - (preço * 5 / 100)

print('O produto que custava R% {:.2f}, na promoção com desconto de 5% vai custa R$ {:.2f}'.format(preço, novo))