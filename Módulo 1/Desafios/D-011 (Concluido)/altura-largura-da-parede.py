altura = float(input('Digite a altura da parede: '))
largura = float(input('Agora digite a largura da parede: '))

area_parede = altura * largura
litros_tinta = area_parede / 2

print(f'Para pintar a parede, você precisará de {litros_tinta:.2f} litros de tinta.')