'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine 
se a mesma é uma data válida.

----------------------------------------------------------------
'''

print('\n* * * VALIDA DATA * * *\n')

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

dia_valido = False
mes_valido = False
ano_valido = False

if dia > 0 and dia <= 31:
    dia_valido = True

if mes > 0 and mes <= 12:
    mes_valido = True

if ano <= 9999:
    ano_valido = True

if dia_valido and mes_valido and ano_valido:
    print(f'\n{str(dia).rjust(2,"0")}/{str(mes).rjust(2,"0")}/{str(ano).rjust(4,"0")} é uma data válida!\n')
else:
    print(f'\n{str(dia).rjust(2,"0")}/{str(mes).rjust(2,"0")}/{str(ano).rjust(4,"0")} é uma data inválida!\n')



