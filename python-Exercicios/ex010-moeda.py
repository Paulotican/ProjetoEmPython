real = float(input('Quanto dinheiro você tem na carteira: R$'))
dolar = real / 4.87
euro = real / 5.26
libra = real / 6.13
print('Com R${:.2f} você pode compra US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode compra €${:.2f}'.format(real, euro))
print('Com R${:.2f} você pode compra £${:.2f}'.format(real, libra))
