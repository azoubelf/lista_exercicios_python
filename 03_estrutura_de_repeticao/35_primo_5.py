'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Encontrar números primos é uma tarefa difícil. Faça um programa que 
gera uma lista dos números primos existentes entre 1 e um número 
inteiro informado pelo usuário.

----------------------------------------------------------------
'''

def eh_primo(num):
    num_divisoes = 0
    numero = num
    copia_num = numero
    divisores = 0
    while num > 0:
        if copia_num % num == 0:
            divisores += 1
        num_divisoes += 1
        num -= 1

    if divisores <= 2:
        return [ True, num_divisoes ]
    return [ False, num_divisoes ]

print('\n* * * PRIMOS V * * *\n')

num = int(input('Deseja saber os números primos entre 1 e...: '))
total_divisoes = 0 

print(f'\nPrimos entre 1 e {num}:\n')

for i in range(1, num + 1):
    if eh_primo(i)[0]:
        print(f'{i}', end = ' ')
        total_divisoes += eh_primo(i)[1]

print()