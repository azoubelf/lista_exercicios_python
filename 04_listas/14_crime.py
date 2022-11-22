'''
Lista de Exercício Python
Listas
Data: 08.11.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Utilizando listas faça um programa que faça 5 perguntas para uma 
pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação 
da pessoa no crime. Se a pessoa responder positivamente a 2 questões 
ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" 
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

----------------------------------------------------------------
'''

print('\n* * * CRIME * * *\n')

perguntas = [
	'Telefonou para a vítima? ',
	'Esteve no local do crime? ',
	'Mora perto da vítima? ',
	'Devia para a vítima? ',
	'Já trabalhou com a vítima? '
]

respostas = []

print('1 - Sim || 0 - Não\n')

for pergunta in perguntas:
	resp = input(f'{pergunta}')

	if resp == '1':
		respostas.append('SIM')
	else:
		respostas.append('NAO')

respostas_positivas = respostas.count('SIM')

if respostas_positivas == 5:
	print('\n* * ASSASSINO * *\n')
elif respostas_positivas == 4  or respostas_positivas == 3:
	print('\n* * CÚMPLICE * *\n')
elif respostas_positivas == 2:
	print('\n* * SUSPEITO * *\n')
else:
	print('\n* * INOCENTE * *\n')