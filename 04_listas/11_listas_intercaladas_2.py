'''
Lista de Exercício Python
Listas
Data: 03.11.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

----------------------------------------------------------------
'''

print('\n* * * TRÊS VETORES * * *\n')

lista_1, lista_2, lista_3, lista_4 = [], [], [], []

for i in range(4):
	num = int(input(f'Digite o {i + 1}º elemento da primeira lista: '))
	lista_1.append(num)

print()

for i in range(4):
	num = int(input(f'Digite o {i + 1}º elemento da segunda lista: '))
	lista_2.append(num)

print()

for i in range(4):
	num = int(input(f'Digite o {i + 1}º elemento da terceira lista: '))
	lista_3.append(num)

for i in range(4):
	lista_4.append(lista_1[i])
	lista_4.append(lista_2[i])
	lista_4.append(lista_3[i])

print(f'''
Primeira lista....: {lista_1}
Segunda lista.....: {lista_2}
Terceira lista....: {lista_3}
Quarta lista......: {lista_4}
''')