'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa que peça os 3 lados de um triângulo. O programa 
deverá informar se os valores podem ser um triângulo. Indique, 
caso os lados formem um triângulo, se o mesmo é: equilátero, 
isósceles ou escaleno.
Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois 
  lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;

----------------------------------------------------------------
'''

print('\n* * * TRIÂNGULOS * * *\n')

lado_1 = int(input('Digite o tamanho do primeiro lado: '))
lado_2 = int(input('Digite o tamanho do segundo lado: '))
lado_3 = int(input('Digite o tamanho do terceiro lado: '))

if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    print('\nTriângulo válido!')
    if lado_1 == lado_2 and lado_1 == lado_3:
        print('Triângulo equilátero.\n')
    elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
        print('Triângulo escaleno')
    else:
        print('Triângulo isósceles')
else:
    print('\nTriângulo inválido!\n')


