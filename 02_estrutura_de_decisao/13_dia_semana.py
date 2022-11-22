'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que leia um número e exiba o dia correspondente 
da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor 
deve aparecer valor inválido.

----------------------------------------------------------------
'''

print('\n* * * DIA DA SEMANA * * *\n')

dia = int(input('Digite um número correspondente ao dia da semana: '))

if dia == 1:
    print('\nDomingo')
elif dia == 2:
    print('\nSegunda-feira')
elif dia == 3:
    print('\nTerça-feira')
elif dia == 4:
    print('\nQuarta-feira')
elif dia == 5:
    print('\nQuinta-feira')
elif dia == 6:
    print('\nSexta-feira')
elif dia == 7:
    print('\nSábado')
else:
    print('\nErro')