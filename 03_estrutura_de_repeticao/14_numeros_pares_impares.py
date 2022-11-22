'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que peça 10 números inteiros, calcule e mostre 
a quantidade de números pares e a quantidade de números impares.

----------------------------------------------------------------
'''

print('\n* * * PARES E ÍMPARES * * *\n')

num_pares = 0
num_impares = 0

for i in range(10):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1

print(f'''
Foram digitados:
{num_pares} números pares
{num_impares} números ímpares
''')
