'''
Lista de Exercício Python
Estrutura Sequencial
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que peça o tamanho de um arquivo para download 
(em MB) e a velocidade de um link de Internet (em Mbps), calcule 
e informe o tempo aproximado de download do arquivo usando este 
link (em minutos).

----------------------------------------------------------------
'''

from math import ceil


print('\n* * * DOWNLOAD * * *\n')

tamanho_arquivo = float(input('Digite o tamanho do arquivo (em MB): '))
velocidade = float(input('Digite a velocidade da internet (MBps): '))

segundos = tamanho_arquivo / velocidade
minutos = ceil(segundos / 60)

print(f'\nO download será concluído em aproximadamente {minutos} minutos\n')
