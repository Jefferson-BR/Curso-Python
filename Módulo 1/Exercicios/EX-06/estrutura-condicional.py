nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))
media = (nota_1 + nota_2) /2

if media >= 5.0:
    print(f"Sua nota final é: {media} a sua média está boa")
else:
    print(f"Sua nota final é: {media} a sua média está ruim")