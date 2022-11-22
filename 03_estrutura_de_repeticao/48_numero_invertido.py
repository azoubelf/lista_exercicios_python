'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que peça um numero inteiro positivo e em seguida 
mostre este numero invertido.
Exemplo:
  12376489
  => 98467321

----------------------------------------------------------------
'''

print('\n* * * NÚMERO INVERTIDO * * *\n')

num = int(input('Digite um número: '))
num = str(num)

print(num[::-1])
print()