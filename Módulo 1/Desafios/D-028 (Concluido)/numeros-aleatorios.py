from random import randint
from time import sleep
import os

numero_aleatorio = randint(0, 5)
resposta = int(input("Qual e sua resposta ? Digite um número: "))
print(f"PROCESSANDO...")
sleep(2)
if resposta == numero_aleatorio:
    print(f"Você Acertou! O Número que o computador escolheu foi: {numero_aleatorio}")
else:
    print(f"Você Errou! O Número que o computador escolheu foi: {numero_aleatorio}")
    video_path = '"C:\\Users\\jeffe\\Documents\\Curso Python\\Módulo 1\\Desafios\\D-028\\else.mp4"'
    os.system(f'"start "" {video_path}"')  # Para Windows
    # os.system(f"open {video_path}")  # Para macOS
    # os.system(f"xdg-open {video_path}")  # Para Linux