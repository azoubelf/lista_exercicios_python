'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que peça um número inteiro e determine se ele é 
par ou impar. Dica: utilize o operador módulo (resto da divisão).

----------------------------------------------------------------
'''

print('\n* * * PAR OU ÍMPAR * * *\n')

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'{numero} é par\n')
else:
    print(f'{numero} é ímpar!\n')
