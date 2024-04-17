dias = int(input('Quantos dias alugados? Digite: '))
km = float(input('Quantos Km rodados? Digite: '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))