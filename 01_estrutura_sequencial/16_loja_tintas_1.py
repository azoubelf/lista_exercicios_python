'''
Lista de Exercício Python
Estrutura Sequencial
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa para uma loja de tintas. O programa deverá pedir 
o tamanho em metros quadrados da área a ser pintada. Considere que 
a cobertura da tinta é de 1 litro para cada 3 metros quadrados e 
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem 
compradas e o preço total.

----------------------------------------------------------------
''' 

from math import ceil


print('\n* * * LOJA DE TINTAS 1 * * *\n')

area = float(input('Digite a área a ser pintada: '))
litros = area / 3

# 3 * 18
if area % 54 == 0:
    latas = area / 54
else:
    latas = ceil(area / 54)

valor = latas * 80

print(f'\nLitros necessários: {ceil(litros)}')
print(f'Total de latas: {latas}')
print(f'Valor final: R$ {valor:.2f}\n')