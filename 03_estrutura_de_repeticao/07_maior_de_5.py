'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que leia 5 números e informe o maior número.

----------------------------------------------------------------
'''

print('\n* * * MAIOR DE 5 * * *\n')

i = 0
maior = None

while i < 5:
    num = int(input('Digite um número: '))
    if maior == None:
        maior = num
    else:
        if num > maior:
            maior = num
    i += 1

print(f'\nMaior número digitado: {maior}\n')