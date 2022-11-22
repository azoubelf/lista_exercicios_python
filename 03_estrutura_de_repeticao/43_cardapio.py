'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades 
desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) 
e o total geral do pedido. Considere que o cliente deve informar quando o 
pedido deve ser encerrado.

----------------------------------------------------------------
'''

print('\n* * * Cardápio * * *\n')

print('''
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
''')

total = 0

while True:
    codigo = int(input('Digite o código [0 para sair]: '))
    if codigo == 0:
        break
    quantidade = int(input('Digite a quantidade de produtos: '))
    
    if codigo == 100:
        total += quantidade * 1.20
    elif codigo == 101:
        total += quantidade * 1.30
    elif codigo == 102:
        total += quantidade * 1.50
    elif codigo == 103:
        total += quantidade * 1.20
    elif codigo == 104:
        total += quantidade * 1.30
    elif codigo == 105:
        total += quantidade * 1
    else:
        print('Código inválido.')

print(f'\nPreço final: R${total:.2f}\n')

