'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer 
número inteiro entre 1 a 10. O usuário deve informar de qual numero ele 
deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50

----------------------------------------------------------------
'''

print('\n* * * TABUADA * * *\n')

num = int(input('Deseja ver a tabuada de: '))

print()

for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')

print()