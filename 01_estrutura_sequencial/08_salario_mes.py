'''
Lista de Exercício Python
Estrutura Sequencial
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que pergunte quanto você ganha por hora e o 
número de horas trabalhadas no mês. Calcule e mostre o total do 
seu salário no referido mês.

----------------------------------------------------------------
''' 

print('\n* * * Salário * * *\n')

horas = int(input('Digite o número de horas trabalhadas: '))
ganho_hora = float(input('Digite o quanto você ganha por hora: '))
salario_final = horas * ganho_hora

print(f'Salário final: R$ {salario_final:.2f}\n')

