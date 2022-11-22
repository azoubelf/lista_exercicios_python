'''
Lista de Exercício Python
Estrutura de Decisão
Data: 26.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

O Hipermercado Tabajara está com uma promoção de carnes que é 
imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas 
um dos tipos de carne da promoção, porém não há limites para a quantidade 
de carne por cliente. Se compra for feita no cartão Tabajara o cliente 
receberá ainda um desconto de 5% sobre o total da compra. Escreva um 
programa que peça o tipo e a quantidade de carne comprada pelo usuário 
e gere um cupom fiscal, contendo as informações da compra: tipo e 
quantidade de carne, preço total, tipo de pagamento, valor do desconto 
e valor a pagar.

----------------------------------------------------------------
'''

print('\n* * * MERCADO * * *')

print('''
TIPOS DE CARNE
1. Filé duplo
2. Alcatra
3. Picanha
''')

escolha = int(input('Selecione a carne [1/2/3]: '))

if escolha == 1 or escolha == 2 or escolha == 3:
    quilos = int(input('Digite a quantidade de carne em kg: '))
    if escolha == 1:
        tipo = 'Filé Duplo'
        if quilos <= 5:
            valor = quilos * 4.9
        else:
            valor = quilos * 5.8
    
    elif escolha == 2:
        tipo = 'Alcatra'
        if quilos <= 5:
            valor = quilos * 5.9
        else:
            valor = quilos * 6.8
    
    elif escolha == 3:
        tipo = 'Picanha'
        if quilos <= 5:
            valor = quilos * 6.9
        else:
            valor = quilos * 7.8
    
    print('''
    TIPOS DE PAGAMENTO:
    1. Cartão
    2. Dinheiro
    ''')

    pagamento = int(input('Selecione o tipo de pagamento [1/2]: '))
    
    if pagamento == 1:
        tipo = 'Cartão'
        desconto = (5/100) * valor
        print(f'''
    Tipo de carne: {tipo}
    Preço total: R$ {valor:.2f}
    Tipo de pagamento: {tipo}
    Desconto: R$ {desconto:.2f}
    Valor final: R$ {(valor - desconto):.2f}
        ''')
    else:
        tipo = 'Dinheiro'
        print(f'''
    Tipo de carne: {tipo}
    Preço total: R$ {valor:.2f}
    Tipo de pagamento: {tipo}
        ''')
