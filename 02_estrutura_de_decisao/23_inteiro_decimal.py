'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que peça um número e informe se o número é inteiro 
ou decimal. Dica: utilize uma função de arredondamento.

----------------------------------------------------------------
'''

print('\n* * * INTEIRO OU DECIMAL * * *\n')

numero = float(input('Digite um número: '))

if numero == round(numero):
    print(f'\n{numero} é inteiro!\n')
else:
    print(f'\n{numero} é decimal!\n')
