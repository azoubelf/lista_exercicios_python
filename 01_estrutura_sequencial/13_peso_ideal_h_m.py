'''
Lista de Exercício Python
Estrutura Sequencial
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Tendo como dado de entrada a altura (h) de uma pessoa, construa 
um algoritmo que calcule seu peso ideal, utilizando as seguintes 
fórmulas:
- Para homens: (72.7*h) - 58
- Para mulheres: (62.1*h) - 44.7

----------------------------------------------------------------
''' 

print('\n* * * PESO IDEAL II * * *\n')

altura = float(input('Digite a sua altura: '))

peso_ideal_homens = (72.7 * altura) - 58
peso_ideal_mulheres = (62.1 * altura) - 44.7

print(f'''
Pesos ideais para a sua altura:
Homens....: {peso_ideal_homens:.1f} kg
Mulheres..: {peso_ideal_mulheres:.1f} kg
''')
