'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

----------------------------------------------------------------
'''

print('\n* * * MASCULINO FEMININO * * *\n')

s = input('Digite o sexo [M/F]: ')

if s == 'M':
    print('\nMasculino.\n')
elif s == 'F':
    print('\nFeminino.\n')
else:
    print('\nInválido\n')