'''
Lista de Exercício Python
Estrutura Sequencial
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Tendo como dados de entrada a altura de uma pessoa, construa um 
algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
(72.7*altura) - 58

----------------------------------------------------------------
''' 

print('\n* * * PESO IDEAL * * *\n')

altura = float(input('Digite a sua altura: '))
peso_ideal = (72.7 * altura) - 58

print(f'\nSeu peso ideal seria: {peso_ideal:.1f}\n')