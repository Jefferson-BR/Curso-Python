nome = input('Qual é o seu nome? ')
sobrenome = input('Escreva seu sobrenome: ')
terceiro_nome = input('Escreva o seu terceiro nome: ')
print('Um prazer em te conhecer {:=^19}!'.format(nome), end=' ')
print('Seu sobrenome é este: {:=>17}!'.format(sobrenome))
print('Seu terceiro nome é este: {:=<16}!'.format(terceiro_nome))

conta_1 = (5 + 5) * 5
conta_2 = (8 + 8) * 2 ** 2
erro = 5 + 5 * 5
print('\n' f'Resultado errado: {erro}')
print (f'Resultado da conta um: {conta_1}, Resultado da conta dois: {conta_2}')
