'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Em uma eleição presidencial existem quatro candidatos. Os votos 
são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
- O total de votos para cada candidato;
- O total de votos nulos;
- O total de votos em branco;
- A  percentagem de votos nulos sobre o total de votos;
- A percentagem de votos em branco sobre o total de votos. 
Para finalizar o conjunto de votos tem-se o valor zero.

----------------------------------------------------------------
'''

print('\n* * * ELEIÇÕES * * *\n')

print('''
CANDIDATOS

1 - João
2 - José
3 - Maria
4 - Ana
5 - Nulo
6 - Branco
''')

cand_1 = 0
cand_2 = 0
cand_3 = 0
cand_4 = 0
nulo = 0
branco = 0
total_votos = 0

while True:
    voto = int(input('Digite o seu voto [0 para sair]: '))
    if voto == 0:
        break
    elif voto == 1:
        cand_1 += 1
    elif voto == 2:
        cand_2 += 1
    elif voto == 3:
        cand_3 += 1
    elif voto == 4:
        cand_4 += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
    else:
        nulo += 1
    total_votos += 1

porc_nulos = (nulo * 100) / total_votos
porc_brancos = (branco * 100) /total_votos
print(f'''
RESULTADO

Total de votos: {total_votos}

João    - {cand_1} votos.
José    - {cand_2} votos.
Maria   - {cand_3} votos.
Ana     - {cand_4} votos.
Nulos   - {nulo} - {porc_nulos:.1f} %
Branos  - {branco} - {porc_brancos:.1f} %
''')