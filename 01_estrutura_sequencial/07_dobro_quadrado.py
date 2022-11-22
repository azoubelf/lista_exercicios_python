'''
Lista de Exercício Python
Estrutura Sequencial
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que calcule a área de um quadrado, em seguida 
mostre o dobro desta área para o usuário.

----------------------------------------------------------------
''' 

print('\n* * * DOBRO DO QUADRADO * * *\n')

lado = float(input('Digite o lado do quadrado: '))
dobro_area = 2 * (lado * lado)

print(f'Dobro da área: {dobro_area:.1f}\n')
