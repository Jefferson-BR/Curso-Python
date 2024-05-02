from math import sqrt

cateto_oposto = float(input('Digite o Cateto Oposto: '))
cateto_adjacente = float(input('Digite o Cateto Adjacente: '))

hipotenusa = sqrt(cateto_oposto**2 + cateto_adjacente**2)

print(f'O calculo da forma é: {hipotenusa:.2f}')