'''
Lista de Exercício Python
Estrutura Sequencial
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que peça a temperatura em graus Fahrenheit, 
transforme e mostre a temperatura em graus Celsius.

----------------------------------------------------------------
''' 

print('\n* * * CONVERSOR DE TEMPERATURA I * * *\n')

fah = float(input('Digite a temperatura em Fahrenheit: '))
cel = 5 * ((fah - 32) / 9)

print(f'\n{fah}°F = {cel}°C\n')

