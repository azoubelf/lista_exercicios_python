'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que peça uma nota, entre zero e dez. Mostre uma 
mensagem caso o valor seja inválido e continue pedindo até que o 
usuário informe um valor válido.

----------------------------------------------------------------
'''

print('\n* * * VALIDA NOTA * * *\n')

while True:
    nota = float(input('Digite uma nota: '))

    if nota >= 0 and nota <= 10:
        print(f'\nNota computada: {nota}\n')
        break
    else:
        print('Digite uma nota válida!\n')