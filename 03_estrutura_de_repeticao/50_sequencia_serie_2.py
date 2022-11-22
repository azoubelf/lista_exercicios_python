'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que 
calcule o valor de H com N termos.

----------------------------------------------------------------
'''

print('\n* * * SEQUÊNCIA II * * *\n')

final = int(input('Digite o final da sequência: '))
soma = 0
inicio = 1

while inicio <= final:
    if inicio != final:
        print(f'1 / {inicio} +', end = ' ')
    else:
        print(f'1 / {inicio} = ', end = ' ')
    soma += (1 / inicio)
    inicio += 1

print(f'{soma:.2f}\n')
