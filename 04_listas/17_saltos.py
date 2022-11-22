'''
Lista de Exercício Python
Listas
Data: 11.11.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Em uma competição de salto em distância cada atleta tem direito
a cinco saltos. O resultado do atleta será determinado pela média
dos cinco valores restantes. Você deve fazer um programa que receba
o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
e depois informe o nome, os saltos e a média dos saltos. O programa
deve ser encerrado quando não for informado o nome do atleta. A saída
do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m

----------------------------------------------------------------
'''

print('\n* * * SALTOS * * *\n')


while True:

    saltos = []
    nome = input('\nDigite o nome do atleta: ')

    if nome == '':
        print('\n* PROGRAMA ENCERRADO *\n')
        break

    for i in range(1, 6):
        salto = float(input(f'Digite o {i}º salto: '))
        saltos.append(salto)

    print(f'''
Atleta: {nome}

Primeiro salto: {saltos[0]}
Segundo salto: {saltos[1]}
Terceiro salto: {saltos[2]}
Quarto salto: {saltos[3]}
Quinto salto: {saltos[4]}
Média dos saltos: {(sum(saltos) / len(saltos)):.1f}
''')

