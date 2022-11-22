'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que peça um número inteiro e determine se ele é 
ou não um número primo. Um número primo é aquele que é divisível 
somente por ele mesmo e por 1.

----------------------------------------------------------------
'''

print('\n* * * PRIMO * * *\n')

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