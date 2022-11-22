'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa para um caixa eletrônico. O programa deverá perguntar 
ao usuário a valor do saque e depois informar quantas notas de cada 
valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 
50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes 
na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas 
notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três 
notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e 
quatro notas de 1.

----------------------------------------------------------------
'''

print('\n* * * CAIXA ELETRÔNICO * * *\n')

valor = int(input('Digite o valor a sacar: '))

if valor >= 10 and valor <= 600:
    notas_100 = valor // 100
    sobra_de_100 = valor - (notas_100 * 100)
    notas_50 = sobra_de_100 // 50
    sobra_de_50 = sobra_de_100 - (notas_50 * 50)
    notas_10 = sobra_de_50 // 10
    sobra_de_10 = sobra_de_50 - (notas_10 * 10)
    notas_5 = sobra_de_10 // 5
    sobra_de_5 = sobra_de_10 - (notas_5 * 5)
    notas_1 = sobra_de_5

    if notas_100 > 0:
        print(f'Notas de 100: {notas_100}')
    if notas_50 > 0:
        print(f'Notas de 50: {notas_50}')
    if notas_10 > 0:
        print(f'Notas de 10: {notas_10}')
    if notas_5 > 0:
        print(f'Notas de 5: {notas_5}')
    if notas_1 > 0:
        print(f'Notas de 1: {notas_1}')
    
else:
    print('\nValor inválido!\n')

