'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que imprima na tela apenas os números ímpares 
entre 1 e 50.

----------------------------------------------------------------
'''

print('\n* * * NÚMEROS ÍMPARES * * *\n')

for i in range(51):
    if i % 2 != 0:
        print(f'{i} é ímpar.')

print()
