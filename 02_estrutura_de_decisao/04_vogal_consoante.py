'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que verifique se uma letra digitada é vogal ou 
consoante.

----------------------------------------------------------------
'''

print('\n* * * VOGAL OU CONSOANTE * * *\n')

letra = input('Digite uma letra: ').upper()

if letra.isalpha() and len(letra) == 1:
    if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        print(f'{letra} é uma vogal.\n')
    else:
        print(f'{letra} é uma consoante.\n')
else:
    print('\nInput inválido.\n')