'''
Lista de Exercício Python
Listas
Data: 31.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que leia 20 números inteiros e armazene-os num 
vetor. Armazene os números pares no vetor PAR e os números IMPARES 
no vetor impar. Imprima os três vetores.

----------------------------------------------------------------
'''

print('\n* * * PARES & ÍMPARES * * *\n')

lista = []

for i in range(20):
	num = int(input('Digite um número: '))
	lista.append(num)

pares = [ num for num in lista if num % 2 == 0 ]
impares = [ num for num in lista if num % 2 != 0 ]

print(f'\nLista total..: {lista}')
print(f'Pares........: {pares}')
print(f'Ímpares......: {impares}\n')
