'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Supondo que a população de um país A seja da ordem de 80000 habitantes 
com uma taxa anual de crescimento de 3% e que a população de B seja 200000 
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que 
calcule e escreva o número de anos necessários para que a população do 
país A ultrapasse ou iguale a população do país B, mantidas as taxas de 
crescimento.

----------------------------------------------------------------
'''

from math import floor


print('\n* * * CRESCIMENTO * * *\n')

populacao_pais_a = 80000
populacao_pais_b = 200000
crescimento_a = (3/100)
crescimento_b = (1.5/100)
ano = 1

while populacao_pais_a < populacao_pais_b:
    print(f'Ano: {ano}')
    populacao_pais_a += (crescimento_a * populacao_pais_a)
    populacao_pais_b += (crescimento_b * populacao_pais_b)
    print(f'População do país A: {floor(populacao_pais_a)}')
    print(f'População do país B: {floor(populacao_pais_b)}')
    ano += 1
