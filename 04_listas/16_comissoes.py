'''
Lista de Exercício Python
Listas
Data: 08.11.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Utilize uma lista para resolver o problema a seguir. Uma empresa 
paga seus vendedores com base em comissões. O vendedor recebe $200 
por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma 
semana recebe $200 mais 9 por cento de $3000, ou seja, um total 
de $470. Escreva um programa (usando um array de contadores) que 
determine quantos vendedores receberam salários nos seguintes 
intervalos de valores:
	$200 - $299
	$300 - $399
	$400 - $499
	$500 - $599
	$600 - $699
	$700 - $799
	$800 - $899
	$900 - $999
	$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir 
do salário, sem fazer vários ifs aninhados.

----------------------------------------------------------------
'''

print('\n* * * COMISSÕES * * *\n')

vendas_brutas = [ 
	200, 240, 250, 290, 360, 808, 818, 820, 909, 929, 
	999, 1000, 1001, 1050, 2000, 3000, 4000, 4500, 4700, 
	5000, 6000, 6500, 6800, 7000, 8000, 9000, 10000, 11000, 
	12200, 13000
]

salarios = [ (200 + (9/100) * venda) for venda in vendas_brutas ]

intervalo_1 = [ salario for salario in salarios if salario >= 200 and salario < 300 ]
intervalo_2 = [ salario for salario in salarios if salario >= 300 and salario < 400 ]
intervalo_3 = [ salario for salario in salarios if salario >= 400 and salario < 500 ]
intervalo_4 = [ salario for salario in salarios if salario >= 500 and salario < 600 ]
intervalo_5 = [ salario for salario in salarios if salario >= 600 and salario < 700 ]
intervalo_6 = [ salario for salario in salarios if salario >= 700 and salario < 800 ]
intervalo_7 = [ salario for salario in salarios if salario >= 800 and salario < 900 ]
intervalo_8 = [ salario for salario in salarios if salario >= 900 and salario < 1000 ]
intervalo_9 = [ salario for salario in salarios if salario >= 1000 ]

print(f'''
Número de vendedores nos intervalos:

$200 - $299				-	{len(intervalo_1)}
$300 - $399				-	{len(intervalo_2)}
$400 - $499				-	{len(intervalo_3)}
$500 - $599				-	{len(intervalo_4)}
$600 - $699				-	{len(intervalo_5)}
$700 - $799				-	{len(intervalo_6)}
$800 - $899				-	{len(intervalo_7)}
$900 - $999				-	{len(intervalo_8)}
$1000 em diante				-	{len(intervalo_9)}
''')