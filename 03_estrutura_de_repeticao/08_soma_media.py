'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que leia 5 números e informe a soma e a média dos números.

----------------------------------------------------------------
'''

print('\n* * * SOMA E MÉDIA * * *\n')

soma = 0

for i in range(5):
    num = int(input(f'Digite o {i + 1}° número: '))
    soma += num

media = soma / 5

print(f'\nSoma: {soma}')
print(f'Média: {media:.1f}\n')