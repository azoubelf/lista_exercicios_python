'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que peça para n pessoas a sua idade, ao final o 
programa devera verificar se a média de idade da turma varia entre 
0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, 
adulta ou idosa, conforme a média calculada.

----------------------------------------------------------------
'''

print('\n* * * MÉDIA DE IDADES * * *\n')

soma = 0
total = 0

while True:
    num = int(input('Digite uma idade [0 para sair]: '))
    if num == 0:
        break
    soma += num
    total += 1

media = soma / total

print(f'\nMédia: {media:.1f}')

if media >= 0 and media <= 25:
    print('A turma é jovem!\n')
elif media > 25 and media <= 60:
    print('A turma é adulta!\n')
elif media > 60:
    print('A turma é idosa!\n')
else:
    print('Erro.\n')
