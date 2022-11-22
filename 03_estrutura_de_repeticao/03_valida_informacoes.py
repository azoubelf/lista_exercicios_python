'''
Lista de Exercício Python
Estrutura de Repetição
Data: 27.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';

----------------------------------------------------------------
'''

print('\n* * * VALIDA INFORMAÇÕES * * *\n')

nome = input('Digite um nome de, pelo menos, 3 caracteres: ')
idade = int(input('Digite a idade: '))
salario = float(input('Digite um salário: '))
sexo = input('Digite o sexo [M/F]: ').upper()
estado_civil = input('Digite o estado civil [S, C, V, D]: ').upper()

while len(nome) < 3:
    nome = input('Digite um nome válido: ')

while idade < 0 or idade > 150:
    idade = int(input('Digite uma idade válida: '))

while salario < 0:
    salario = float(input('Digite um salário válido: '))
    
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite um sexo válido: ').upper()

while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
    estado_civil = input('Digite um estado civil válido: ').upper()

print(f'''
Nome: {nome}
Idade: {idade}
Salário: R$ {salario:.2f}
Sexo: {sexo}
Estado civil: {estado_civil}
''')