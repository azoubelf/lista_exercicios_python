'''
Lista de Exercício Python
Listas
Data: 31.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

----------------------------------------------------------------
'''

print('\n* * * MÉDIA * * *\n')

notas = []

for i in range(1, 5):
	nota = float(input(f'Digite a {i}ª nota: '))
	notas.append(nota)

media = sum(notas) / len(notas)

print(f'\nMédia final: {media:.1f}\n')
