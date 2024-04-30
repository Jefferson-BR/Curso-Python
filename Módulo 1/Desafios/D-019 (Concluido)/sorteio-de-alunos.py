import random

aluno_1 = input('Digite O nome do primeiro aluno: ')
aluno_2 = input('Digite O nome do segundo aluno: ')
aluno_3 = input('Digite O nome do terceiro aluno: ')
aluno_4 = input('Digite O nome do quarto aluno: ')

alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
aluno_sorteado = random.choice(alunos)

print(f"O Aluno sorteado é: {aluno_sorteado}")