'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Desenvolver um programa para verificar a nota do aluno em uma prova 
com 10 questões, o programa deve perguntar ao aluno a resposta de
cada questão e ao final comparar com o gabarito da prova e assim 
calcular o total de acertos e a nota (atribuir 1 ponto por resposta 
certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta 
se outro aluno vai utilizar o sistema. Após todos os alunos terem 
respondido informar:
- Maior e Menor Acerto;
- Total de Alunos que utilizaram o sistema;
- A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que 
o professor digite o gabarito da prova antes dos alunos usarem o programa.

----------------------------------------------------------------
'''

print('\n* * * PROVA * * *\n')

aluno_mais_acertos = None
nota_mais_acertos = None
aluno_menos_acertos = None
nota_menos_acertos = None
total_alunos = 0
total_acertos = 0

while True:
    aluno = input('Digite o nome do aluno [S para sair]: ')
    acertos_aluno = 0
    if aluno == 'S':
        break
    for i in range(1, 11):
        resp = input(f'Digite a resposta da {i}ª questão: ').upper()
        if (i == 1 and resp == 'A'):
            acertos_aluno += 1
        if i == 2 and resp == 'B':
            acertos_aluno += 1
        if i == 3 and resp == 'C':
            acertos_aluno += 1
        if i == 4 and resp == 'D':
            acertos_aluno += 1
        if i == 5 and resp == 'E':
            acertos_aluno += 1
        if i == 6 and resp == 'E':
            acertos_aluno += 1
        if i == 7 and resp == 'D':
            acertos_aluno += 1
        if i == 8 and resp == 'C':
            acertos_aluno += 1
        if i == 9 and resp == 'B':
            acertos_aluno += 1
        if i == 10 and resp == 'A':
            acertos_aluno += 1
    
    if aluno_mais_acertos == None:
        aluno_mais_acertos = aluno
        nota_mais_acertos = acertos_aluno
    else:
        if acertos_aluno > nota_mais_acertos:
            aluno_mais_acertos = aluno
            nota_mais_acertos = acertos_aluno
    
    if aluno_menos_acertos == None:
        aluno_menos_acertos = aluno
        nota_menos_acertos = acertos_aluno
    else:
        if acertos_aluno < nota_menos_acertos:
            aluno_menos_acertos = aluno
            nota_menos_acertos = acertos_aluno
    total_acertos += acertos_aluno
    total_alunos += 1

media = total_acertos / total_alunos

print(f'''
RESULTADOS

Total de alunos: {total_alunos}

Mais acertos:
- Nome: {aluno_mais_acertos}
- Nota: {nota_mais_acertos}

Menos acertos:
- Nome: {aluno_menos_acertos}
- Nota: {nota_menos_acertos}

Média da turma: {media:.1f}
''')