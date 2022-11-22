'''
Lista de Exercício Python
Listas
Data: 03.11.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que peça a idade e a altura de 5 pessoas, armazene 
cada informação no seu respectivo vetor. Imprima a idade e a altura 
na ordem inversa a ordem lida.

----------------------------------------------------------------
'''

print('\n* * * IDADES & ALTURAS * * *\n')

dados = []

for i in range(1, 6):
	nome = input(f'\nDigite o nome da {i}ª pessoa: ')
	idade = int(input(f'Digite a idade da {i}ª pessoa: '))
	altura = float(input(f'Digite a altura da {i}ª pessoa: '))

	dados.append([ nome, idade, altura ])

dados_reverso = dados[::-1]

for dado in dados_reverso:
	print(f'\nIdade: {dado[1]}')
	print(f'Altura: {dado[2]}')