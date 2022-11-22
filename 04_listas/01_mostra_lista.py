'''
Lista de Exercício Python
Listas
Data: 31.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

----------------------------------------------------------------
'''

print('\n* * * MOSTRA LISTA * * *\n')

lista_numeros = []

for i in range(5):
	num = int(input('Digite um número: '))
	lista_numeros.append(num)

print(f'\nLista: {lista_numeros}\n')