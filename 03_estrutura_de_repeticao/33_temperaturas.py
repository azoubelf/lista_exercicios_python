'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

O Departamento Estadual de Meteorologia lhe contratou para desenvolver 
um programa que leia as um conjunto indeterminado de temperaturas, e 
informe ao final a menor e a maior temperaturas informadas, bem como a 
média das temperaturas.

----------------------------------------------------------------
'''

print('\n* * * TEMPERATURAS * * *\n')

maior = None
menor = None
soma = 0
total = 0

while True:
    temperatura = int(input('Digite uma temperatura: '))
    soma += temperatura
    total += 1
    if maior == None:
        maior = temperatura
    else:
        if temperatura > maior:
            maior = temperatura
    
    if menor == None:
        menor = temperatura
    else:
        if temperatura < menor:
            menor = temperatura
    
    sair = int(input('Digite [0] para sair: '))
    if sair == 0:
        break

media = soma / total

print(f'''
TEMPERATURAS

Menor temperatura......: {menor}° C
Maior temperatura......: {maior}° C
Média de temperaturas..: {media:.1f}° C
''')