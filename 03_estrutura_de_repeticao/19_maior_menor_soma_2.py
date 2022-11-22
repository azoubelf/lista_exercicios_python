'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Altere o programa anterior para que ele aceite apenas números entre 
0 e 1000.

----------------------------------------------------------------
'''

print('\n* * * MAIOR, MENOR, SOMA II * * *\n')

tamanho = int(input('Digite o tamanho do conjunto: '))
maior = None
menor = None
soma = 0

print()

for i in range(1, tamanho + 1):
    while True:
        num = int(input(f'Digite o {i}º número: '))
        if num > 0 and num <= 1000:
            break
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
