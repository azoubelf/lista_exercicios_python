'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que peça dois números, base e expoente, calcule e 
mostre o primeiro número elevado ao segundo número. Não utilize a 
função de potência da linguagem.

----------------------------------------------------------------
'''

print('\n* * * BASE E EXPOENTE * * *\n')

base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))
copia_base = base

for i in range(1, expoente):
    copia_base *= base

print(copia_base)
print(base)

