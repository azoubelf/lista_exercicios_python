'''
Lista de Exercício Python
Listas
Data: 03.11.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que leia dois vetores com 10 elementos cada. Gere 
um terceiro vetor de 20 elementos, cujos valores deverão ser compostos
pelos elementos intercalados dos dois outros vetores.

----------------------------------------------------------------
'''

print('\n* * * DOIS VETORES * * *\n')

lista_1 = []
lista_2 = []
lista_3 = []

for i in range(10):
	num = int(input(f'Digite o {i + 1}º elemento da primeira lista: '))
	lista_1.append(num)

print()

for i in range(10):
	num = int(input(f'Digite o {i + 1}º elemento da segundaa lista: '))
	lista_2.append(num)

for i in range(10):
	lista_3.append(lista_1[i])
	lista_3.append(lista_2[i])

print(f'''
Primeira lista....: {lista_1}
Segunda lista.....: {lista_2}
Terceira lista....: {lista_3}
''')