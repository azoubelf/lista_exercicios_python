'''
Lista de Exercício Python
Listas
Data: 03.11.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Foram anotadas as idades e alturas de 30 alunos. Faça um Programa 
que determine quantos alunos com mais de 13 anos possuem altura 
inferior à média de altura desses alunos.

----------------------------------------------------------------
'''

print('\n* * * IDADES E ALTURAS * * *\n')

dados = []

for i in range(30):
	nome = input('\nDigite o nome: ')
	idade = int(input('Digite a idade: '))
	altura = float(input('Digite a altura: '))

	dados.append([ nome, idade, altura ])

soma_alturas = 0

for i in range(len(dados)):
	soma_alturas += dados[i][2]

media_alturas = soma_alturas / len(dados)

menores_media = [ aluno for aluno in dados if ((aluno[1] > 13) and (aluno[2] < media_alturas)) ]

print(f'\nMédia das alturas: {media_alturas:.1f}')

print('Alunos com altura menor que a média:\n')

for dado in menores_media:
	print(f'\nNome: {dado[0]}')
	print(f'Idade: {dado[1]}')
	print(f'Altura: {dado[2]:.1f}')

print()
