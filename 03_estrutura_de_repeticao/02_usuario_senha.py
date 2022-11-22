'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que leia um nome de usuário e a sua senha e não 
aceite a senha igual ao nome do usuário, mostrando uma mensagem 
de erro e voltando a pedir as informações.

----------------------------------------------------------------
'''

print('\n* * * USUÁRIO E SENHA * * *\n')

while True:
    usuario = input('Digite o usuário: ')
    senha = input('Digite a senha: ')

    if usuario == senha:
        print('\nUsuário e senha precisam ser diferentes!\n')
    else:
        print('\nUsuário e senha aceitos!\n')
        break

