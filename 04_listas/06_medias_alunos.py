'''
Lista de Exercício Python
Listas
Data: 31.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que peça as quatro notas de 10 alunos, calcule 
e armazene num vetor a média de cada aluno, imprima o número de 
alunos com média maior ou igual a 7.0.

----------------------------------------------------------------
'''

print('\n* * * MÉDIAS * * *\n')

medias = []

for i in range(10):
	notas = []
	print('\nNovo aluno\n')
	for i in range(1, 5):
		nota = float(input(f'Digite a {i}ª nota: '))
		notas.append(nota)
	medias.append((sum(notas) / len(notas)))

aprovados = [ media for media in medias if media >= 7]
print(f'\nTodas as médias....: {medias}')	
print(f'Alunos aprovados...: {aprovados}\n')


