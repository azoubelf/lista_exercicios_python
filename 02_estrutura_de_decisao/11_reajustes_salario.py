'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

As Organizações Tabajara resolveram dar um aumento de salário aos 
seus colaboradores e lhe contraram para desenvolver o programa que 
calculará os reajustes. Faça um programa que recebe o salário de 
um colaborador e o reajuste segundo o seguinte critério, baseado 
no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
> o salário antes do reajuste;
> o percentual de aumento aplicado;
> o valor do aumento;
> o novo salário, após o aumento.

----------------------------------------------------------------
'''

print('\n* * * REAJUSTES SALARIAIS * * *\n')

salario = float(input('Digite o salário do colaborador: '))

if salario <= 280:
    percentual = 20
elif salario > 280 and salario <= 700:
    percentual = 15
elif salario > 700 and salario <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = (percentual / 100) * salario
salario_final = salario + aumento

print(f'''
RESULTADOS

Salário inicial.........: R$ {salario:.2f}
Percentual de aumento...: {percentual}%
Valor do aumento........: R$ {aumento:.2f}
Salário final...........: R$ {salario_final:.2f}
''')