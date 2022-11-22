'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa para o cálculo de uma folha de pagamento, sabendo 
que os descontos são do Imposto de Renda, que depende do salário bruto 
(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde 
a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O 
programa deverá pedir ao usuário o valor da sua hora e a quantidade de 
horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a 
quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00

----------------------------------------------------------------
'''

print('\n* * * FOLHA DE PAGAMENTO * * *\n')

valor_hora = float(input('Digite o valor por hora trabalhada: '))
horas = int(input('Digite o número de horas trabalhadas: '))

salario_bruto = valor_hora * horas

if salario_bruto <= 900:
    desc = 0
elif salario_bruto > 900 and salario_bruto <= 1500:
    desc = 5
elif salario_bruto > 1500 and salario_bruto <= 2500:
    desc = 10
elif salario_bruto > 2500:
    desc = 20

desconto_ir = (desc/100) * salario_bruto
mensagem_desc = f"(-) IR ({desc} %)"

desconto_inss = (10/100) * salario_bruto
fgts = (11/100) * salario_bruto
total_descontos = desconto_inss + desconto_ir

salario_liquido = salario_bruto - total_descontos
desc_str = str(desc)

print(f'''
RESULTADOS

    {"Salário bruto": <20}:   R$ {salario_bruto:.2f}
    {mensagem_desc:<20}:   R$ {desconto_ir:.2f}
    {"(-) INSS (10%)":<20}:   R$ {desconto_inss:.2f}
    {"FGTS (11%)":<20}:   R$ {fgts:.2f}
    {"Total de Descontos":<20}:   R$ {total_descontos:.2f}
    {"Salário Líquido":<20}:   R$ {salario_liquido:.2f}
''')