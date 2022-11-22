'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que leia 2 números e em seguida pergunte ao usuário 
qual operação ele deseja realizar. O resultado da operação deve ser 
acompanhado de uma frase que diga se o número é:
- par ou ímpar;
- positivo ou negativo;
- inteiro ou decimal.

----------------------------------------------------------------
'''

from unittest import result


print('\n* * * SUPER OPERAÇÕES * * *\n')

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))

operacao = input('Escolha uma operação [+, -, *, /]: ')
operacao_valida = False

if operacao == '+':
    resultado = num_1 + num_2
    operacao_valida = True
elif operacao == '-':
    resultado = num_1 - num_2
    operacao_valida = True
elif operacao == '*':
    resultado = num_1 * num_2
    operacao_valida = True
elif operacao == '/':
    resultado = num_1 / num_2
    operacao_valida = True
else:
    print('\nOperação inválida!\n')

if operacao_valida:
    print(f'\nResultado: {resultado}')

    if resultado % 2 == 0:
        print('O resultado é par!')
    else:
        print('O resultado é ímpar!')
    
    if resultado >= 0:
        print('O resultado é positivo!')
    else:
        print('O resultado é negativo!')
    
    if resultado == round(resultado):
        print('O resultado é inteiro!\n')
    else:
        print('O resultado é decimal!\n')

