'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que leia um número inteiro menor que 1000 e imprima 
a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre 
outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades 
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 
20, 10, 21, 11, 1, 7 e 16

----------------------------------------------------------------
'''

print('\n* * * CENTENAS, DEZENAS, UNIDADES * * *\n')

def divide_numero(numero):
    tem_centena = False
    tem_dezena = False
    tem_unidade = False
    centenas = numero // 100
    dezenas_restantes = numero - (centenas * 100)
    dezenas = dezenas_restantes // 10
    unidades = dezenas_restantes - (dezenas * 10)

    # print(f'Centenas: {centenas}')
    # print(f'Dezenas: {dezenas}')
    # print(f'Unidades: {unidades}')

    if centenas > 0:
        tem_centena = True
        if centenas > 1:
            mensagem_centena = f'{centenas} centenas'
        elif centenas == 1:
            mensagem_centena = f'{centenas} centena'

    if dezenas > 0:
        tem_dezena = True
        if dezenas > 1:
            mensagem_dezena = f'{dezenas} dezenas'
        elif dezenas == 1:
            mensagem_dezena = f'{dezenas} dezena'

    if unidades > 0:
        tem_unidade = True
        if unidades > 1:
            mensagem_unidade = f'{unidades} unidades'
        elif unidades == 1:
            mensagem_unidade = f'{unidades} unidade'

    if tem_centena and tem_dezena and tem_unidade:
        print(f'{numero}: {mensagem_centena}, {mensagem_dezena} e {mensagem_unidade}')

    if tem_centena and tem_dezena and not tem_unidade:
        print(f'{numero}: {mensagem_centena} e {mensagem_dezena}')

    if tem_centena and tem_unidade and not tem_dezena:
        print(f'{numero}: {mensagem_centena} e {mensagem_unidade}')

    if tem_centena and not tem_dezena and not tem_unidade:
        print(f'{numero}: {mensagem_centena}')

    if not tem_centena and tem_dezena and tem_unidade:
        print(f'{numero}: {mensagem_dezena} e {mensagem_unidade}')

    if not tem_centena and tem_dezena and not tem_unidade:
        print(f'{numero}: {mensagem_dezena}')

    if not tem_centena and not tem_dezena and tem_unidade:
        print(f'{numero}: {mensagem_unidade}')


divide_numero(326)
divide_numero(300)
divide_numero(320)
divide_numero(100)
divide_numero(310)
divide_numero(305)
divide_numero(301)
divide_numero(101)
divide_numero(311)
divide_numero(111)
divide_numero(25)
divide_numero(20)
divide_numero(21)
divide_numero(16)
divide_numero(11)
divide_numero(1)
divide_numero(7)

print()