'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que calcule o fatorial de um número inteiro 
fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

----------------------------------------------------------------
'''

print('\n* * * FATORIAL * * *\n')

fat = int(input('Deseja descobrir o fatorial de: '))
resultado = 1

while fat >= 1:
    resultado *= fat
    fat -= 1

print(f'Resultado: {resultado}')