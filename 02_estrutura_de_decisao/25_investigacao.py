'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:
1. "Telefonou para a vítima?"
2. "Esteve no local do crime?"
3. "Mora perto da vítima?"
4. "Devia para a vítima?"
5. "Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação 
da pessoa no crime. Se a pessoa responder positivamente a 2 questões 
ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" 
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

----------------------------------------------------------------
'''

print('\n* * * INVESTIGAÇÃO * * *\n')

numero_positivos = 0

tel = input('Telefonou para a vítima [s/n]? ').upper()
local = input('Esteve no local do crime [s/n]? ').upper()
mora = input('Mora perto da vítima [s/n]? ').upper()
devia = input('Devia para a vítima [s/n]? ').upper()
trab = input('Trabalhava com a vítima [s/n]? ').upper()

if tel == 'S':
    numero_positivos += 1
if local == 'S':
    numero_positivos += 1
if mora == 'S':
    numero_positivos += 1
if devia == 'S':
    numero_positivos += 1
if trab == 'S':
    numero_positivos += 1

print(f'\nRespostas positivas: {numero_positivos}')

if numero_positivos == 2:
    print('Pessoa suspeita!\n')
elif numero_positivos == 3 or numero_positivos == 4:
    print('Pessoa cúmplice!\n')
elif numero_positivos == 5:
    print('Pessoa assassina!\n')
else:
    print('Pessoa inocente!\n')
