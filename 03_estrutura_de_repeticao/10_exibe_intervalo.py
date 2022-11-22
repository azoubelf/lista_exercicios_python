'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que receba dois números inteiros e gere os números 
inteiros que estão no intervalo compreendido por eles.

----------------------------------------------------------------
'''

print('\n* * * INTERVALO * * *\n')

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))

if num_1 < num_2:
    while num_1 <= num_2:
        print(num_1)
        num_1 += 1
elif num_1 > num_2:
    while num_1 >= num_2:
        print(num_1)
        num_1 -= 1
else:
    print('Por favor, digite números diferentes.')
