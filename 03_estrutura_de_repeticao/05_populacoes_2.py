'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Altere o programa anterior permitindo ao usuário informar as populações 
e as taxas de crescimento iniciais. Valide a entrada e permita repetir 
a operação.

----------------------------------------------------------------
'''
print('\n* * * CRESCIMENTO II * * *\n')

pop_cidade_1 = int(input('Digite a população da primeira cidade: '))
taxa_crescimento_c1 = int(input('Digite a taxa de crescimento (%): '))

ano = 1

while True:
    pop_cidade_2 =  int(input('Digite a população da segunda cidade: '))
    taxa_crescimento_c2 = int(input('Digite a taxa de crescimento (%): '))

    if pop_cidade_2 < pop_cidade_1 or taxa_crescimento_c2 > taxa_crescimento_c1:
        print('\nA população da segunda cidade precisa ser maior e a taxa de crescimento precisa ser menor.')
    else:
        break

while pop_cidade_1 < pop_cidade_2:
    print(f'\nAno: {ano}')
    pop_cidade_1 += (taxa_crescimento_c1/100) * pop_cidade_1
    pop_cidade_2 += (taxa_crescimento_c2/100) * pop_cidade_2
    print(f'Cidade 1: {pop_cidade_1}')
    print(f'Cidade 2: {pop_cidade_2}')
    ano += 1
