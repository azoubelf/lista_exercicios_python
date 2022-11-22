'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que leia uma quantidade indeterminada de números 
positivos e conte quantos deles estão nos seguintes intervalos: [0-25], 
[26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando 
for lido um número negativo.

----------------------------------------------------------------
'''

print('\n* * * INTERVALOS * * *\n')

intervalo_1 = 0
intervalo_2 = 0
intervalo_3 = 0
intervalo_4 = 0

while True:
    num = int(input('Digite um número: '))
    if num >= 0 and num <= 25:
        intervalo_1 += 1
    elif num > 25 and num <= 50:
        intervalo_2 += 1
    elif num > 50 and num <= 75:
        intervalo_3 += 1
    elif num > 75 and num <= 100:
        intervalo_4 += 1
    elif num < 0:
        break

print(f'''
RESULTADOS

Intervalo 01 - [00 - 25]  - {intervalo_1}
Intervalo 02 - [26 - 50]  - {intervalo_2}
Intervalo 03 - [51 - 75]  - {intervalo_3}
Intervalo 04 - [76 - 100] - {intervalo_4}
''')