'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que leia três números e mostre-os em ordem 
decrescente.

----------------------------------------------------------------
'''

print('\n* * * ORDEM DECRESCENTE * * *\n')

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
num_3 = int(input('Digite o terceiro número: '))

maior = None
menor = None
meio = None

if num_1 != num_2 and num_1 != num_3 and num_2 != num_3:
    if num_1 > num_2 and num_1 > num_2:
        maior = num_1
        if num_2 > num_3:
            meio = num_2
            menor = num_3
        else:
            meio = num_3
            menor = num_2

    if num_2 > num_1 and num_2 > num_3:
        maior = num_2
        if num_1 > num_3:
            meio = num_1
            menor = num_3
        else:
            meio = num_3
            menor = num_1
        
    if num_3 > num_1 and num_3 > num_2:
        maior = num_3
        if num_1 > num_2:
            meio = num_1
            menor = num_2
        else:
            meio = num_2
            menor = num_1

    print(f'\n{maior} - {meio} - {menor}\n')

else:
    print('\nDigite números diferentes.\n')