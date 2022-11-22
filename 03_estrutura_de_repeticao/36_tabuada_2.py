'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Desenvolva um programa que faça a tabuada de um número qualquer 
inteiro que será digitado pelo usuário, mas a tabuada não deve 
necessariamente iniciar em 1 e terminar em 10, o valor inicial 
e final devem ser informados também pelo usuário, conforme 
exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor 
que o inicial.

----------------------------------------------------------------
'''

print('\n* * * TABUADA II * * *\n')

tabuada = int(input('Deseja montar a tabuada de: '))
inicio = int(input('Deseja começar por: '))
while True:
    fim = int(input('Deseja terminar em: '))
    if fim >= inicio:
        break
    print('Por favor, digite um número maior que o início.')

for i in range(inicio, fim + 1):
    print(f'{tabuada} x {i} = {tabuada * i}')