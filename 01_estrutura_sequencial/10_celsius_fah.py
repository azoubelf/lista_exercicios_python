'''
Lista de Exercício Python
Estrutura Sequencial
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que peça a temperatura em graus Celsius, 
transforme e mostre em graus Fahrenheit.

----------------------------------------------------------------
''' 

print('\n* * * CONVERSOR DE TEMPERATURA II * * *\n')

cel = float(input('Digite a temperatur em Celsius: '))
fah = (cel * 1.8) + 32

print(f'\n{cel}°C = {fah}°F\n')


