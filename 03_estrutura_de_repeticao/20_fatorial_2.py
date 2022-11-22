'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Altere o programa de cálculo do fatorial, permitindo ao usuário 
calcular o fatorial várias vezes e limitando o fatorial a números 
inteiros positivos e menores que 16.

----------------------------------------------------------------
'''

print('\n* * * FATORIAL II * * *\n')

while True:
    while True:
        fat = int(input('\nDeseja descobrir o fatorial de: '))
        if fat > 0 and fat < 16:
            break
        else:
            print('\nDigite um número válido [1-16].\n')
    resultado = 1

    while fat >= 1:
        resultado *= fat
        fat -= 1

    print(f'Resultado: {resultado}')

    sair = int(input('\nDigite 1 para continuar ou 0 para sair: '))
    if sair == 0:
        print('\n* * PROGRAMA ENCERRADO * *\n')
        break