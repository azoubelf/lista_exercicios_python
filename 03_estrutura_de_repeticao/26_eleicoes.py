'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Numa eleição existem três candidatos. Faça um programa que peça o 
número total de eleitores. Peça para cada eleitor votar e ao final 
mostrar o número de votos de cada candidato.

----------------------------------------------------------------
'''

print('\n* * * ELEIÇÕES * * *\n')

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
invalidos = 0

total_eleitores = int(input('Digite o total de eleitores: '))

for i in range(total_eleitores):
    voto = int(input('Selecione um candidato [1, 2, 3]: '))
    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    else:
        invalidos += 1

print(f'''
RESULTADOS

Candidato 1.....: {candidato_1}
Candidato 2.....: {candidato_2}
Candidato 3.....: {candidato_3}
Inválidos.......: {invalidos}
''')

