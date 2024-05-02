largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area_parede = largura * altura
litros_tinta = area_parede / 2

print(f'Sua parede tem a dimensão de: {largura}x{altura} e a sua área é de {area_parede}m², para pintar a parede sera necessario ter {litros_tinta:.2f} litros de tinta.')