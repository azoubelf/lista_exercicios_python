'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que pergunte o preço de três produtos e informe 
qual produto você deve comprar, sabendo que a decisão é sempre 
pelo mais barato.

----------------------------------------------------------------
'''

print('\n* * * PRODUTO MAIS BARATO * * *\n')

prod_1 = float(input('Digite o valor do primeiro produto: '))
prod_2 = float(input('Digite o valor do segundo produto: '))
prod_3 = float(input('Digite o valor do terceiro produto: '))

if prod_1 != prod_2 and prod_1 != prod_3 and prod_2 != prod_3:
    if prod_1 < prod_2 and prod_1 < prod_3:
        print('\nO primeiro produto é o mais barato!\n')
    
    if prod_2 < prod_1 and prod_2 < prod_3:
        print('\nO segundo produto é o mais barato!\n')
    
    if prod_3 < prod_1 and prod_3 < prod_2:
        print('\nO terceiro produto é o mais barato!\n')
        
else:
    print('\nDigite valores diferentes!\n')
    