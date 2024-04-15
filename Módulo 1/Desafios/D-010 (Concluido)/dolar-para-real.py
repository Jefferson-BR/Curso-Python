valor = float(input('Quanto você tem na carteira ? Digite o Valor em Dolar US$: '))

conversao = valor * 5.18 # Preço do dolar baseado na data (15/04/2024)
print(f'Com US$ {valor} você consegue comprar R$ {conversao}')

valor_reais = float(input('Quanto você tem na carteira? Digite o valor em Reais R$: '))

taxa_cambio_dolar_para_real = 5.18
taxa_cambio_real_para_dolar = 1 / taxa_cambio_dolar_para_real

valor_dolares = valor_reais * taxa_cambio_real_para_dolar

print(f'Com R$ {valor_reais} você consegue comprar US$ {valor_dolares:.2f}')
