'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos 
para cada turma. As turmas não podem ter mais de 40 alunos.

----------------------------------------------------------------
'''

print('\n* * * MÉDIA DE ALUNOS POR TURMA * * *\n')

quantidade_turmas = int(input('Digite a quantidade de turmas: '))
soma = 0
i = 1

while i <= quantidade_turmas:
    alunos = int(input(f'Digite a quantidade de alunos da {i}ª turma: '))
    if alunos <= 40:
        soma += alunos
        i += 1
    else:
        print('Turma não pode ter mais de 40 alunos.')

media = soma / quantidade_turmas

print(f'\nNúmero médio de alunos: {media:.1f}\n')