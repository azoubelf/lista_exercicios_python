'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Em uma competição de ginástica, cada atleta recebe votos de sete 
jurados. A melhor e a pior nota são eliminadas. A sua nota fica 
sendo a média dos votos restantes. Você deve fazer um programa 
que receba o nome do ginasta e as notas dos sete jurados alcançadas 
pelo atleta em sua apresentação e depois informe a sua média, 
conforme a descrição acima informada (retirar o melhor e o pior 
salto e depois calcular a média com as notas restantes). As notas 
não são informados ordenadas. Um exemplo de saída do programa deve 
ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04

----------------------------------------------------------------
'''

print('\n* * * GINÁSTICA * * *\n')

atleta = input('Digite o nome do atleta: ')
notas = []

for i in range(1, 8):
    nota = float(input(f'Digite a {i}ª nota: '))
    notas.append(nota)

novas_notas = notas.copy()

novas_notas.remove(max(novas_notas))
novas_notas.remove(min(novas_notas))
media = sum(novas_notas) / len(novas_notas)

print(f'''
RESULTADO

Atleta: {atleta}

Nota 1: {notas[0]}
Nota 2: {notas[1]}
Nota 3: {notas[2]}
Nota 4: {notas[3]}
Nota 5: {notas[4]}
Nota 6: {notas[5]}
Nota 7: {notas[6]}

Melhor nota: {max(notas)}
Pior nota: {min(notas)}

Média final: {media:.1f}
''')