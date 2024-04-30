from math import sin, cos, tan, radians

angulo = float(input("Digite o valor do ângulo em graus: "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"Seno do ângulo: {seno:.2f}")
print(f"Cosseno do ângulo: {cosseno:.2f}")
print(f"Tangente do ângulo: {tangente:.2f}")