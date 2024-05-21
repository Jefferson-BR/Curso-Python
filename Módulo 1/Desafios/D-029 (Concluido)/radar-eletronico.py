from time import sleep
print("Faltam 500 metros para chegar no radar...")
sleep(1)
print("Faltam 400 metros para chegar no radar...")
sleep(1)
print("Faltam 300 metros para chegar no radar...")
sleep(1)
print("Faltam 200 metros para chegar no radar...")
sleep(1)
print("Faltam 100 metros para chegar no radar...")
sleep(1)

vel = int(input('Qual a velocidade que o carro passou no radar? Km/h: '))
print("Verificando a velocidade [...]")
sleep(2)
if vel > 80:
    multa = (vel - 80) * 7
    print(f"Você estava a {vel}Km/h e foi multado. O valor da multa é R${multa:.2f} Respeite os limites da via! Boa Viagem!")
else:
    print(f"Sua velocidade no radar foi {vel}Km/h, permaneça respeitando os limites da via. Boa Viagem!")