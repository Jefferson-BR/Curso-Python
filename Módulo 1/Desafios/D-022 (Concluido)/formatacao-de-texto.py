nome = str(input("Digite seu nome ou uma palavra: ")).strip()
remocao = nome.replace(" ", "")
print("Analisando Seu nome...")
print(f"\n Se Ele for escrito em maiúscula vai ficar assim: {nome.upper()}\n Se Ele for escrito em minúscula vai ficar assim: {nome.lower()}\n Seu nome contem: {len(remocao)} letras\n E por fim seu primeiro nome contem: {nome.find(' ')} letras")

# Segunda forma de fazer a contagem do primeiro nome
separacao = nome.split()
print(f"\nSeu Primeiro nome contem: {separacao[0]} {len(separacao[0])} letras")