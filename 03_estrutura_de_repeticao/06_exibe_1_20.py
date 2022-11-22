'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que imprima na tela os números de 1 a 20, um 
abaixo do outro. Depois modifique o programa para que ele mostre 
os números um ao lado do outro.

----------------------------------------------------------------
'''

print('\n* * * Exibe números * * *\n')

for i in range(1, 21):
    print(i)


for i in range(1, 21):
    print(i, end = ' ')
