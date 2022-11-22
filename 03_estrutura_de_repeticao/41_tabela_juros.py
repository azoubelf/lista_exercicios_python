'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que receba o valor de uma dívida e mostre uma 
tabela com os seguintes dados: valor da dívida, valor dos juros, 
quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67

----------------------------------------------------------------
'''

print('\n* * * DÍVIDA! * * *\n')

divida = float(input('Digite o valor da dívida: '))

juros = 0
parcelas = 1

for i in range(5):
    valor_final = divida + ((juros/100) * divida)
    valor_parcela = valor_final / parcelas
    print(f'Dívida: R$ {valor_final:.2f} | Juros: {juros:0<2}% | Parcelas {parcelas:0>2} | Valor parcela: R$ {valor_parcela:.2f}')
    if juros == 0:
        juros += 10
        parcelas += 2
    else: 
        juros += 5
        parcelas += 3

print()