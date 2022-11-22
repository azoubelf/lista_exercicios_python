'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que peça um valor e mostre na tela se o valor 
é positivo ou negativo.

----------------------------------------------------------------
'''

print('\n* * * POSITIVO NEGATIVO * * *\n')

numero = int(input('Digite um número: '))

if numero < 0:
    print(f'{numero} é negativo.\n')
else:
    print(f'{numero} é positivo.\n')

