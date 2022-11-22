'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que leia dez conjuntos de dois valores, o primeiro 
representando o número do aluno e o segundo representando a sua altura 
em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o 
número do aluno mais alto e o número do aluno mais baixo, junto com 
suas alturas.

----------------------------------------------------------------
'''

print('\n* * * ALTURAS ALUNOS * * *\n')

codigo_mais_alto = None
altura_mais_alto = None
codigo_mais_baixo = None
altura_mais_baixo = None

for i in range(10):
    codigo = int(input('Digite o código do aluno: '))
    altura = int(input('Digite a altura do aluno [em cm]: '))

    # Mais alto
    if codigo_mais_alto == None:
        codigo_mais_alto = codigo
        altura_mais_alto = altura
    else:
        if altura > altura_mais_alto:
            codigo_mais_alto = codigo
            altura_mais_alto = altura
    
    # Mais baixo
    if codigo_mais_baixo == None:
        codigo_mais_baixo = codigo
        altura_mais_baixo = altura
    else:
        if altura < altura_mais_baixo:
            codigo_mais_baixo = codigo
            altura_mais_baixo = altura

print(f'''
RESULTADOS

Aluno mais alto............: {codigo_mais_alto}
Altura do aluno mais alto..: {altura_mais_alto} cm

Aluno mais baixo...........: {codigo_mais_baixo}
Altura do aluno mais baixo.: {altura_mais_baixo} cm
''')

