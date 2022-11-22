'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que peça um número correspondente a um determinado 
ano e em seguida informe se este ano é ou não bissexto.

----------------------------------------------------------------
'''

print('\n* * * BISSEXTO * * *\n')

ano = int(input('Digite um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'\n{ano} é bissexto!\n')
else:
    print(f'\n{ano} não é bissexto!\n')
