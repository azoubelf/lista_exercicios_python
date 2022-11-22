'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que pergunte em que turno você estuda. Peça para 
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem 
"Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", 
conforme o caso.

----------------------------------------------------------------
'''

print('\n* * * TURNOS * * *\n')

print('''
OPÇÕES:

M - Matutino
V - Vespertino
N - Noturno
''')

turno = input('Digite um turno [M/V/N]: ').upper()

if turno == 'M':
    print('\nBom dia!\n')
elif turno == 'V':
    print('\nBoa tarde!\n')
elif turno == 'N':
    print('\nBoa noite!\n')
else:
    print('\nTurno inválido!\n')
