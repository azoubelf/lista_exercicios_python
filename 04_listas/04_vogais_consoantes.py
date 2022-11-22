'''
Lista de Exercício Python
Listas
Data: 31.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que leia um vetor de 10 caracteres, e diga quantas 
consoantes foram lidas. Imprima as consoantes.

----------------------------------------------------------------
'''

print('\n* * * VOGAIS E CONSOANTES * * *\n')

vogais = [ 'a', 'e', 'i', 'o', 'u' ]
consoantes = []

for i in range(10):
	letra = input('Digite uma letra: ')
	if letra.isalpha() and letra not in vogais:
		consoantes.append(letra)

print(f'\nConsoantes digitadas: {consoantes}\n')