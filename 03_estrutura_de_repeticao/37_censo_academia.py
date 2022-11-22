'''
Lista de Exercício Python
Estrutura de Repetição
Data: 28.10.2022
Estudante: Filipe G. Azoubel

----------------------------------------------------------------

Uma academia deseja fazer um senso entre seus clientes para descobrir 
o mais alto, o mais baixo, a mais gordo e o mais magro, para isto 
você deve fazer um programa que pergunte a cada um dos clientes da 
academia seu código, sua altura e seu peso. O final da digitação de 
dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores 
do clente mais alto, do mais baixo, do mais gordo e do mais magro, além 
da média das alturas e dos pesos dos clientes

----------------------------------------------------------------
'''

print('\n* * * ACADEMIA * * *\n')

soma_alturas = 0
soma_pesos = 0
total_clientes = 0

codigo_mais_alto = None
codigo_mais_baixo = None
altura_mais_alto = None
altura_mais_baixo = None

codigo_mais_gordo = None
codigo_mais_magro = None
peso_mais_gordo = None
peso_mais_magro = None

while True:
    codigo = int(input('Digite o código do cliente [0 para sair]: '))
    if codigo == 0:
        break
    altura = float(input('Digite a altura do cliente: '))
    peso = float(input('Digite o peso do cliente: '))

    soma_alturas += altura
    soma_pesos += peso
    total_clientes += 1

    # Mais alto
    if codigo_mais_alto == None:
        codigo_mais_alto = codigo
        altura_mais_alto = altura
    else:
        if altura > altura_mais_alto:
            codigo_mais_alto = codigo
            altura_mais_alto = altura
    
    # Mais baixo
    if codigo_mais_baixo == None:
        codigo_mais_baixo = codigo
        altura_mais_baixo = altura
    else:
        if altura < altura_mais_baixo:
            codigo_mais_baixo = codigo
            altura_mais_baixo = altura
    
    # Mais gordo
    if codigo_mais_gordo == None:
        codigo_mais_gordo = codigo
        peso_mais_gordo = peso
    else:
        if peso > peso_mais_gordo:
            codigo_mais_gordo = codigo
            peso_mais_gordo = peso
    
    # Mais magro
    if codigo_mais_magro == None:
        codigo_mais_magro = codigo
        peso_mais_magro = peso
    else:
        if peso < peso_mais_magro:
            codigo_mais_magro = codigo
            peso_mais_magro = peso


media_alturas = soma_alturas / total_clientes
media_pesos = soma_pesos / total_clientes

print(f'''
RESULTADOS

Total de clientes..............: {total_clientes}
Média das alturas..............: {media_alturas:.1f}
Média dos pesos................: {media_pesos:.1f}

Cliente mais alto..............: {codigo_mais_alto}
Altura do cliente mais alto....: {altura_mais_alto} m

Cliente mais baixo.............: {codigo_mais_baixo}
Altura do cliente mais baixo...: {altura_mais_baixo} m

Cliente mais gordo.............: {codigo_mais_gordo}
Peso do cliente mais gordo.....: {peso_mais_gordo} kg

Cliente mais magro.............: {codigo_mais_magro}
Peso do cliente mais magro.....: {peso_mais_magro} kg
''')