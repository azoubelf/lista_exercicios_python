'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Foi feita uma estatística em cinco cidades brasileiras para coletar 
dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
- Código da cidade;
- Número de veículos de passeio (em 1999);
- Número de acidentes de trânsito com vítimas (em 1999). 

Deseja-se saber:
- Qual o maior e menor índice de acidentes de transito e a que cidade 
  pertence;
- Qual a média de veículos nas cinco cidades juntas;
- Qual a média de acidentes de trânsito nas cidades com menos de 2.000 
  veículos de passeio.

----------------------------------------------------------------
'''

print('\n* * * CIDADES * * *\n')

codigo_menor_indice = None
codigo_maior_indice = None
maior_indice = None
menor_indice = None

total_veiculos = 0
total_cidades_menos_2000 = 0
acidentes_menos_2000 = 0

for i in range(5):
  codigo = int(input('Digite o código da cidade: '))
  num_veiculos = int(input('Digite o número de veículos: '))
  num_acidentes = int(input('Digite o número de acidentes: '))

  if num_veiculos < 2000:
    total_cidades_menos_2000 += 1
    acidentes_menos_2000 += num_acidentes

  total_veiculos += num_veiculos

  if codigo_maior_indice == None:
    codigo_maior_indice = codigo
    maior_indice = num_acidentes
  else:
    if num_acidentes > maior_indice:
      codigo_maior_indice = codigo
      maior_indice = num_acidentes
  
  if codigo_menor_indice == None:
    codigo_menor_indice = codigo
    menor_indice = num_acidentes
  else:
    if num_acidentes < menor_indice:
      codigo_menor_indice = codigo
      menor_indice = num_acidentes

media_todas_cidades = total_veiculos / 5
media_acidentes_menos_2000 = acidentes_menos_2000 / total_cidades_menos_2000

print(f'''
RESULTADOS

Cidade com maior índice: 
- Código: {codigo_maior_indice}
- Índice: {maior_indice}

Cidade com menor índice:
- Código: {codigo_menor_indice}
- Índice: {menor_indice}

Média de veículos nas cinco cidades:
{media_todas_cidades:.1f}

Média de acidentes nas cidades com menos de 2000 habitantes:
{media_acidentes_menos_2000:.1f}
''')

