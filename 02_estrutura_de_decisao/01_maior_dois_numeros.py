'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que peça dois números e imprima o maior deles.

----------------------------------------------------------------
'''

print('\n* * * MAIOR DE DOIS NÚMEROS * * *\n')

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

if numero_1 > numero_2:
    print(f'\nO primeiro número ({numero_1}) é maior.\n')
else:
    print(f'\nO segundo número ({numero_2}) é maior.\n')