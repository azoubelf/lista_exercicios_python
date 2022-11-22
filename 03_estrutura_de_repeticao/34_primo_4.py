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

print('\n* * * PRIMO IV * * *\n')

num = int(input('Digite um número: '))

copia_numero = num
divisores = 0

while num > 0:
    if copia_numero % num == 0:
        divisores += 1
    num -= 1

if divisores <= 2:
    print(f'\n{copia_numero} é primo.\n')
else:
    print(f'\n{copia_numero} não é primo.\n')