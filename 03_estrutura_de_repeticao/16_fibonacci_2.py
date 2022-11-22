'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,
34,55,... Faça um programa que gere a série até que o valor seja 
maior que 500.

----------------------------------------------------------------
'''

print('\n* * * FIBONACCI II * * *\n')

primeiro = 1
segundo = 1

print(f'{primeiro}\n{segundo}')

prox = 0
while prox < 500:
    prox = primeiro + segundo
    segundo = primeiro
    primeiro = prox
    print(prox)