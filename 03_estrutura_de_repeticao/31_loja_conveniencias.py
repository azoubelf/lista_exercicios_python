'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios 
de 1,99 e agora possui uma loja de conveniências. Faça um programa 
que implemente uma caixa registradora rudimentar. O programa deverá 
receber um número desconhecido de valores referentes aos preços das 
mercadorias. Um valor zero deve ser informado pelo operador para 
indicar o final da compra. O programa deve então mostrar o total 
da compra e perguntar o valor em dinheiro que o cliente forneceu, 
para então calcular e mostrar o valor do troco. Após esta operação, 
o programa deverá voltar ao ponto inicial, para registrar a próxima 
compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...

----------------------------------------------------------------
'''
print('\n* * * LOJA DE CONVENIÊNCIAS * * *\n')

produtos = []
total = 0
i = 0

while True:
    preco = float(input(f'Digite o preço do {i + 1}º produto [0 para sair]: '))
    if preco == 0:
        break

    produtos.append([i + 1, preco])
    total += preco
    i += 1

print('\nRESULTADO\n')

for produto in produtos:
    print(f'Produto {produto[0]} - R$ {produto[1]:.2f} ')
    
print(f'\nTOTAL: R$ {total:.2f}')

dinheiro = float(input('Digite o dinheiro entregue pelo cliente: '))
troco = dinheiro - total

print(f'\nTroco: R$ {troco:.2f}\n')
