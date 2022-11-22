'''
Lista de Exercício Python
Listas
Data: 31.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que leia um vetor de 5 números inteiros, mostre 
a soma, a multiplicação e os números.

----------------------------------------------------------------
'''

print('\n* * * SOMA E MULTIPLICAÇÃO * * *\n')

numeros = []
soma = 0
mult = 1

for i in range(1, 6):
	num = int(input(f'Digite o {i}º número: '))
	numeros.append(num)

for numero in numeros:
	soma += numero 	# poderia usar sum(numeros) também
	mult *= numero

print(f'\nSoma...........: {soma}')
print(f'Multiplicação..: {mult}\n' )