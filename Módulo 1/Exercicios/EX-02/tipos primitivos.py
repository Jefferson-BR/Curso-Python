# Solicita ao usuário que insira um valor inteiro e armazena na variável "inteiro"
inteiro = int(input('Digite um valor inteiro: '))

# Solicita ao usuário que insira um valor real e armazena na variável "real"
real = float(input('Digite um valor real: '))

# Solicita ao usuário que insira um valor lógico (True ou False) e armazena na variável "logico"
# No entanto, a função input() sempre retorna uma string, então o valor lógico será convertido para bool posteriormente
logico = bool(input('Digite um valor lógico: '))

# Solicita ao usuário que insira um texto e armazena na variável "texto"
texto = str(input('Digite um texto: '))

# Imprime os valores das variáveis "inteiro", "real", "logico" e "texto"
# Utiliza a função format() para formatar a saída dos valores
print('{}, {}, {}, {}'.format(inteiro, real, logico, texto))

# Imprime os tipos das variáveis "inteiro", "real", "logico" e "texto"
# Utiliza a função type() para obter o tipo de cada variável
print(type(inteiro), type(real), type(logico), type(texto))
