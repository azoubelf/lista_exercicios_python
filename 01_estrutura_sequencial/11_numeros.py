'''
Lista de Exercício Python
Estrutura Sequencial
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que peça 2 números inteiros e um número real. 
Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo .
- a soma do triplo do primeiro com o terceiro.
- o terceiro elevado ao cubo

----------------------------------------------------------------
''' 

print('\n* * * NÚMEROS * * *\n')

inteiro_1 = int(input('Digite um número inteiro: '))
inteiro_2 = int(input('Digite outro número inteiro: '))
n_real = float(input('Digite um número real: '))

print(f'\nDobro do primeiro vezes metade do segundo: {(inteiro_1 * 2) * (inteiro_2 / 2)}')
print(f'Triplo do primeiro mais terceiro: {(3 * inteiro_1) + n_real}')
print(f'Terceiro elevado ao cubo: {n_real ** 3}\n')
