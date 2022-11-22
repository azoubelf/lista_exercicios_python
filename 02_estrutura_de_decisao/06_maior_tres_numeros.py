'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que leia três números e mostre o maior deles.

----------------------------------------------------------------
'''

print('\n* * * MAIOR DE TRÊS NÚMEROS * * *\n')

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
num_3 = int(input('Digite o terceiro número: '))

maior = None

if num_1 != num_2 and num_1 != num_3 and num_2 != num_3:
    if num_1 > num_2 and num_1 > num_3:
        maior = num_1

    if num_2 > num_1 and num_2 > num_3:
        maior = num_2

    if num_3 > num_1 and num_3 > num_2:
        maior = num_3
    
    print(f'\nO maior número é {maior}.\n')
else:
    print('\nPor favor, digite números diferentes.\n')
