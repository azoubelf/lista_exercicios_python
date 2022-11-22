'''
Lista de Exercício Python
Estrutura Sequencial
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

João Papo-de-Pescador, homem de bem, comprou um microcomputador 
para controlar o rendimento diário de seu trabalho. Toda vez que 
ele traz um peso de peixes maior que o estabelecido pelo regulamento 
de pesca do estado de São Paulo (50 quilos) deve pagar uma multa 
de R$ 4,00 por quilo excedente. João precisa que você faça um 
programa que leia a variável peso (peso de peixes) e calcule o 
excesso. Gravar na variável excesso a quantidade de quilos além 
do limite e na variável multa o valor da multa que João deverá 
pagar. Imprima os dados do programa com as mensagens adequadas.

----------------------------------------------------------------
''' 

print('\n* * * MULTA PESCARIA * * *\n')

quilos = int(input('Digite o peso pescado: '))
excesso = quilos - 50

if excesso > 0:
    multa = excesso * 4
    print(f'\nMultado! Valor da multa: R$ {multa:.2f}\n')
else:
    print(f'\nNão foi multado!\n')