'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que, dado um conjunto de N números, determine o 
menor valor, o maior valor e a soma dos valores.

----------------------------------------------------------------
'''

print('\n* * * MAIOR, MENOR, SOMA * * *\n')

tamanho = int(input('Digite o tamanho do conjunto: '))
maior = None
menor = None
soma = 0

print()

for i in range(1, tamanho + 1):
    num = int(input(f'Digite o {i}º número: '))
    if maior == None:
        maior = num
    else:
        if num > maior:
            maior = num
    
    if menor == None:
        menor = num
    else:
        if num < menor:
            menor = num
    
    soma += num

print(f'''
Maior número: {maior}
Menor número: {menor}
Soma: {soma}
''')
