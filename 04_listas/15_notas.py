'''
Lista de Exercício Python
Listas
Data: 08.11.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que leia um número indeterminado de valores, 
correspondentes a notas, encerrando a entrada de dados quando for 
informado um valor igual a -1 (que não deve ser armazenado). Após 
esta entrada de dados, faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um 
   ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, 
   um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;

----------------------------------------------------------------
'''

print('\n* * * NOTAS * * *\n')

notas = []

conta_notas = 1

while True:
	nota = float(input(f'Digite a {conta_notas}ª nota: '))
	if nota == -1:
		break
	notas.append(nota)
	conta_notas += 1

notas_inversas = notas[::-1]
soma = sum(notas)
media = soma / len(notas)
acima_media = [ nota for nota in notas if nota > media ]
abaixo_sete = [ nota for nota in notas if nota < 7]

print(f'''

Total de notas.........: {len(notas)}
Notas..................: {notas}
Notas (ordem inversa)..:''')

for nota in notas_inversas:
	print(nota)

print(f'''Média..................: {media:.1f}
Acima da média.........: {acima_media}
Abaixo de sete.........: {abaixo_sete}
	''')
