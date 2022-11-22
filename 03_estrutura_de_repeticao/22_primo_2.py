'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Altere o programa de cálculo dos números primos, informando, caso 
o número não seja primo, por quais número ele é divisível.

----------------------------------------------------------------
'''

print('\n* * * PRIMOS II * * *\n')

num = int(input('Digite um número: '))
copia_num = num
divs = []

while num > 0:
    if copia_num % num == 0:
        divs.append(num)
    num -= 1

if len(divs) > 2:
    print(f'\nNão é primo.\nDivisores: {divs}')
else:
    print(f'\n{copia_num} é primo!\n')


