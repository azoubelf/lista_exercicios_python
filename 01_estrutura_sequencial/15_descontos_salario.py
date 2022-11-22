'''
Lista de Exercício Python
Estrutura Sequencial
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que pergunte quanto você ganha por hora e o 
número de horas trabalhadas no mês. Calcule e mostre o total do
seu salário no referido mês, sabendo-se que são descontados 11% 
para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.

----------------------------------------------------------------
''' 

print('\n* * * DESCONTOS SALÁRIO * * *\n')

horas_trabalhadas = int(input('Digite o número de horas trabalhadas: '))
valor_hora = float(input('Digite o valor ganho por hora trabalhada: '))

salario_bruto = horas_trabalhadas * valor_hora

desconto_ir = (11/100) * salario_bruto
desconto_inss = (8/100) * salario_bruto
desconto_sindicato = (5/100) * salario_bruto

salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato

print(f'''
RESULTADOS:

Salário bruto.......: R$ {salario_bruto:.2f}
Desconto IR.........: R$ {desconto_ir:.2f}
Desconto INSS.......: R$ {desconto_inss:.2f}
Desconto Sindicato..: R$ {desconto_sindicato:.2f}

Salário Líquido.....: R$ {salario_liquido:.2f}
''')