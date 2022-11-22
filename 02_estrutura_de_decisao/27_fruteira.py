'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra 
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade 
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

----------------------------------------------------------------
'''

print('\n* * * FRUTEIRA * * *\n')

qtd_morangos = int(input('Digite a quantidade em kg de morangos: '))
qtd_macas = int(input('Digite a quantidade em kg de maçãs: '))

if qtd_morangos <= 5:
    preco_morangos = 2.5 * qtd_morangos
else:
    preco_morangos = 2.2 * qtd_morangos

if qtd_macas <= 5:
    preco_macas = 1.80 * qtd_macas
else:
    preco_macas = 1.50 * qtd_macas

total_kg = qtd_morangos + qtd_macas
total_preco = preco_morangos + preco_macas

if total_kg >= 8 or total_preco >= 25:
    print('\nTem desconto!!!')
    desconto = (10/100) * total_preco
    total_preco = total_preco - desconto

print(f'''
Morangos: {qtd_morangos}kg -   R$ {preco_morangos:.2f}
Maçãs: {qtd_macas}kg -   R$ {preco_macas:.2f}
Preço final: R$ {total_preco:.2f}
''')