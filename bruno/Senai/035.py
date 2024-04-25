# Escreva um programa que leia o
# Nome, idade e sexo de 4 pessoas. No final mostre:
#
# A média de idade do grupo
# Qual é o homem mais velho
# Quantas mulheres têm menos de 20 anos

soma = 0
idade_homem_mais_velho = None
Quant_Mulheres_menor_20_anos = 0

for ele in range(0, 4):
    nome = input('Digiete seu nome: ').strip()
    idade = int(input('Digiete sua idade: '))
    sexo = input('Digiete seu gênero (M/F): ').strip().upper()


#1
soma += idade

#2

if idade_homem_mais_velho == None and sexo == 'M':
    idade_homem_mais_velho = idade
    nome_homem_mais_velho = nome

if idade > idade_homem_mais_velho and sexo == 'M':
    idade_homem_mais_velho = idade
    nome_homem_mais_velho = nome

if sexo == 'F' and idade < 20:
    Quant_Mulheres_menor_20_anos += 1

print('----------------------------------------')
print(f'A média de idade é {soma/4}'
      f'\nO homem mais velho é {nome_homem_mais_velho}'
      f'\nA quantidade de mulheres com menos de 20 anos {Quant_Mulheres_menor_20_anos}')



