'''
Lista de Exercício Python
Listas
Data: 03.11.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que receba a temperatura média de cada mês do ano 
e armazene-as em uma lista. Após isto, calcule a média anual das 
temperaturas e mostre todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 
2 – Fevereiro, . . . ).

----------------------------------------------------------------
'''

print('\n* * * TEMPERATURAS * * *\n')

temperaturas = []
meses = [ 
	'Janeiro', 'Fevereiro', 'Março',
	'Abril', 'Maio', 'Junho',
	'Julho', 'Agosto', 'Setembro',
	'Outubro', 'Novembro', 'Dezembro'
]

soma_temperaturas = 0

for i in range(1, 13):
	temperatura = float(input(f'Digite a temperatura média de {meses[i-1]}: '))
	temperaturas.append([ i, meses[i-1], temperatura])

	soma_temperaturas += temperatura

media_temperaturas = soma_temperaturas / len(temperaturas)

maiores_que_media = [ [ temperatura[1],  temperatura[2] ] for temperatura in temperaturas if temperatura[2] > media_temperaturas ]


print(f'\nMédia das temperaturas: {media_temperaturas}')
print('\nTemperaturas acima da média:\n')

for temp in maiores_que_media:
	print(f'Mês: {temp[0].ljust(12)} | Temperatura: {temp[1]}')