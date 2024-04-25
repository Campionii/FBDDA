# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
#
# Qual é o total gasto na compra
# Quantos produtos custam mais de R$1000,00
# Qual é o produto mais barato


soma = 0
quant_maior_1000 = 0
menor = None

while True:
    produto = input('Produto [sair para encerrar]')
    if produto == 'sair':
        break

    preco = float(input('Preço: '))
    if menor == None:
        menor = preco
        nome_prod_barato = produto

    soma += preco

if preco > 1000:
    quant_maior_1000 += 1

print(f'A soma é {soma}'
      f'\nA quantidade de produtos mais caro que R$1000 é {quant_maior_1000}'
      f'\nO produto mais barato é {nome_prod_barato}')