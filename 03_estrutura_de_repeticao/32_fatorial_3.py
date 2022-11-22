'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que calcule o fatorial de um número inteiro 
fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser 
conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120

----------------------------------------------------------------
'''
print('\n* * * FATORIAL III * * *\n')

fat = int(input('Deseja descobrir o fatorial de: '))
resultado = 1

print(f'\n{fat}! =', end = ' ')

while fat >= 1:
    resultado *= fat
    if fat >= 2:
        print(f'{fat} x', end =' ')
    else:
        print(f'{fat} =', end = ' ')
    fat -= 1
print(f'{resultado}\n')