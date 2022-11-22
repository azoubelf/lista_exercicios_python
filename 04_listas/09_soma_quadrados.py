'''
Lista de Exercício Python
Listas
Data: 03.11.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que leia um vetor A com 10 números inteiros, calcule 
e mostre a soma dos quadrados dos elementos do vetor.

----------------------------------------------------------------
'''

print('\n* * * SOMA DOS QUADRADOS * * *\n')

numeros = []

for i in range(1, 11):
	num = int(input(f'Digite o {i}º número: '))
	numeros.append(num)


# poderia ser sum([numero ** 2 for numero in numeros ])
# escolhi separar para poder imprimir todas as partes

quadrados_numeros = [ numero ** 2 for numero in numeros ]
soma_quadrados = sum(quadrados_numeros)

print(f'''
Números digitados.......: {numeros}
Quadrados dos números...: {quadrados_numeros}
Soma dos quadrados......: {soma_quadrados}
''')