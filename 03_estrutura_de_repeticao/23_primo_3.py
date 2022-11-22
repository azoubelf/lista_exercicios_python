'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que mostre todos os primos entre 1 e N sendo N 
um número inteiro fornecido pelo usuário. O programa deverá mostrar 
também o número de divisões que ele executou para encontrar os números 
primos. Serão avaliados o funcionamento, o estilo e o número de testes 
(divisões) executados.

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

print('\n* * * PRIMOS III * * *\n')

num = int(input('Deseja saber os números primos entre 1 e...: '))
total_divisoes = 0 

print(f'\nPrimos entre 1 e {num}:\n')

for i in range(1, num + 1):
    if eh_primo(i)[0]:
        print(f'{i}', end = ' ')
        total_divisoes += eh_primo(i)[1]

print(f'\n\nTotal de divisões: {total_divisoes}\n')