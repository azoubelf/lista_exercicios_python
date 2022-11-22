'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Altere o programa anterior para mostrar no final a soma dos números.

----------------------------------------------------------------
'''

print('\n* * * INTERVALO II * * *\n')

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))

soma = 0

if num_1 < num_2:
    while num_1 <= num_2:
        print(num_1)
        soma += num_1
        num_1 += 1
elif num_1 > num_2:
    while num_1 >= num_2:
        print(num_1)
        soma += num_1
        num_1 -= 1
else:
    print('Por favor, digite números diferentes.')

print(f'\nSoma: {soma}\n')