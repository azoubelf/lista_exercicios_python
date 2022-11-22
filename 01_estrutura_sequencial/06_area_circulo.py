'''
Lista de Exercício Python
Estrutura Sequencial
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que peça o raio de um círculo, calcule e mostre 
sua área.

----------------------------------------------------------------
'''

import math


print('\n* * * ÁREA DO CÍRCULO * * *\n')

raio = float(input('Digite o raio: '))

area = math.pi * (raio ** 2)
print(f'Área do círculo: {area:.2f}\n')