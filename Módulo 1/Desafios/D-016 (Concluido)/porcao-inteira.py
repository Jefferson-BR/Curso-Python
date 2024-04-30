from math import ceil, floor

numero_real = float(input('Digite Um Número Real: '))
proporcao_acima = ceil(numero_real)
proporcao_abaixo = floor(numero_real)
print(' A proporção desse número: {}\n se arredondado para cima fica: {}\n se arredondado para baixo fica: {}'.format(numero_real, proporcao_acima, proporcao_abaixo))