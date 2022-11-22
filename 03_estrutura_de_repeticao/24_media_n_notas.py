'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que calcule o mostre a média aritmética de N notas.

----------------------------------------------------------------
'''

print('\n* * * MÉDIA ARITMÉTICA * * *\n')

total_numeros = 0
soma = 0

while True:
    num = float(input('Digite uma nota [0 para sair]: '))
    if num == 0:
        break
    total_numeros += 1
    soma += num

media = soma / total_numeros

print(f'\nMédia: {media:.1f}\n')