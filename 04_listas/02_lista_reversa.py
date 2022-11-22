'''
Lista de Exercício Python
Listas
Data: 31.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que leia um vetor de 10 números reais e mostre-
os na ordem inversa.

----------------------------------------------------------------
'''

print('\n* * * LISTA REVERSA * * *\n')

lista = []

for i in range(10):
	num = int(input('Digite um número: '))
	lista.append(num)

print(f'\nLista..........: {lista}')
print(f'Lista reversa..: {lista[::-1]}\n')