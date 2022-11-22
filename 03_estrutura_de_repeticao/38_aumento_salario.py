'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Um funcionário de uma empresa recebe aumento salarial anualmente: 
Sabe-se que:
- Esse funcionário foi contratado em 1995, com salário inicial de 
  R$ 1.000,00;
- Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
- A partir de 1997 (inclusive), os aumentos salariais sempre correspondem 
  ao dobro do percentual do ano anterior. 

Faça um programa que determine o salário atual desse funcionário. Após 
concluir isto, altere o programa permitindo que o usuário digite o salário 
inicial do funcionário.

----------------------------------------------------------------
'''

print('\n* * * AUMENTO SALARIO * * *\n')

ano_atual = int(input('Digite o ano atual: '))
salario_inicial = float(input('Digite o salario inicial: '))

aumento = 1.5
ano_inicial = 1996

while ano_inicial < ano_atual:
    novo_salario = salario_inicial + ((aumento / 100) * salario_inicial)
    print(f'\nAno: {ano_inicial}')
    print(f'Aumento: {int(aumento)}%')
    print(f'Novo salário: R$ {novo_salario:.2f}')
    aumento *= 2
    ano_inicial += 1

print(f'\nSalário final: R$ {novo_salario:.2f}\n')