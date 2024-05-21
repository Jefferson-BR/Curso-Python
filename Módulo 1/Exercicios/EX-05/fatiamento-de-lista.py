frase = str("Curso em Video Python")

manipulacao = frase[9:21:2]
manipulacao_2 = frase[9:21]
manipulacao_3 = frase[:5]
manipulacao_4 = frase[15:]
manipulacao_5 = frase[9::3]
print(f"{manipulacao, manipulacao_2, manipulacao_3, manipulacao_4, manipulacao_5}")

print(f"A Frase Possui: {len(frase)} Caracteres")
print(f"A letra O se repete {frase.count('o', 0, 14)} vezes")

print(f"{frase.find('Python')}")
print(f"{'Curso' in frase}")

print(f"{frase.replace('Python', 'Android')}")
print(f"{frase.title()}")

print(f"{frase.upper(), frase.lower(), frase.capitalize()}")