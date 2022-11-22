'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,
55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

----------------------------------------------------------------
'''

print('\n* * * FIBONACCI I * * *\n')

primeiro = 1
segundo = 1

num = int(input('Deseja gerar a sequência até o nº termo: '))

if num == 1 or num == 2:
    print(1)
else:
    print(f'{primeiro}\n{segundo}')
    for i in range(2, num):
        prox = primeiro + segundo
        segundo = primeiro
        primeiro = prox
        print(prox)