'''
Lista de Exercício Python
Estrutura Sequencial
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Faça um Programa para uma loja de tintas. O programa deverá pedir 
o tamanho em metros quadrados da área a ser pintada. Considere que 
a cobertura da tinta é de 1 litro para cada 6 metros quadrados e 
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os 
respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja 
  menor. Acrescente 10% de folga e sempre arredonde os valores para 
  cima, isto é, considere latas cheias.

----------------------------------------------------------------
'''

from math import ceil


print('\n* * * LOJA DE TINTAS II * * *\n')

area = float(input('Digite a área a ser pintada: '))
litros = (area + (10/100) * area) / 6

# Apenas latas
latas = ceil(litros / 18)
valor_latas = latas * 80

# Apenas galões
galoes = ceil(litros / 3.6)
valor_galoes = galoes * 25

# Mistura
latas_mistura = litros // 18
litros_faltando = litros - (latas_mistura * 18)
galoes_mistura = ceil(litros_faltando / 3.6)
valor_mistura = (latas_mistura * 80) + (galoes_mistura * 25) 

print(f'''
* * RESULTADO * *

Área a ser pintada........: {area}
Litros necessários........: {litros:.1f}

Apenas Latas (18L):
Latas necessárias.........: {latas}
Valor a pagar.............: R$ {valor_latas:.2f}

Apenas galões (3.6L):
Galões necessários........: {galoes}
Valor a pagar.............: R$ {valor_galoes:.2f}

Mistura
Latas necessárias.........: {latas_mistura}
Galões necessários........: {galoes_mistura}
Valor a pagar.............: R$ {valor_mistura}
''')