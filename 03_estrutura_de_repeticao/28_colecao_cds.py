'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que calcule o valor total investido por um colecionador 
em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário 
deverá informar a quantidade de CDs e o valor para em cada um.

----------------------------------------------------------------
'''

print('\n* * * COLEÇÃO DE CDS * * *\n')

quantidade_cds = int(input('Digite a quantidade de CDs: '))
total = 0

for i in range(quantidade_cds):
    valor = float(input(f'Digite o valor do {i + 1}º CD: '))
    total += valor

print(f'''
RESULTADO

Total de CDS.: {quantidade_cds}
Valor total..: R$ {total:.2f}
Média........: R$ {(total / quantidade_cds):.2f}
''')
