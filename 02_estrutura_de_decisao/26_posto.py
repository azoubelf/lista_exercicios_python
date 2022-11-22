'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
- até 20 litros, desconto de 3% por litro
- acima de 20 litros, desconto de 5% por litro
Gasolina:
- até 20 litros, desconto de 4% por litro
- acima de 20 litros, desconto de 6% por litro 

Escreva um algoritmo que leia o número de litros vendidos, o tipo 
de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o 
preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

----------------------------------------------------------------
'''

print('\n* * * POSTO DE COMBUSTÍVEIS * * *\n')

tipo = input('Digite o tipo de combustível [A/G]: ').upper()

if tipo == 'A' or tipo == 'G':
    litros = int(input('Digite a quantidade de litros: '))

    if tipo == 'A':
        valor_litro = 1.90
        if litros <= 20:
            desconto = valor_litro * (3/100)
        else:
            desconto = valor_litro * (5 / 100)
        
    else:
        valor_litro = 2.50
        if litros <= 20:
            desconto = valor_litro * (4/100)
        else:
            desconto = valor_litro * (6/100)

    valor_final = (valor_litro - desconto) * litros
    print(f'\nValor final: R${valor_final:.2f}\n')
else:
    print('\nTipo inválido!\n')