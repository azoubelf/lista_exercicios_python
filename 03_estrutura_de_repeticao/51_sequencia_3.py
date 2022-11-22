'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 

----------------------------------------------------------------
'''

print('\n* * * SEQUÊNCIA III * * *\n')

final = int(input('Deseja a sequência até: '))

n = 1
m = 1
soma = 0

while n <= final:
    if n != final:
        print(f'{n}/{m} + ', end = '')
    else:
        print(f'{n}/{m} ', end = '')
    soma += n / m
    n += 1
    m += 2

print(f'= {soma:.1f}\n')