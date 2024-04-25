# #Crie um programa que leia o nome completo de uma pessoa e mostre:
#1- O nome com todas as letras maiúsculas
#2- O nome com todas minúsculas
#3- Quantas letras ao todo (sem considerar os espaços)
#4- Quantas letras tem o primeiro nome

nome = str(input('Qual o seu nome? ')).strip()


print(nome.lower())
print(nome.upper())
Quant = len(nome.replace('', ''))

nome = nome.split()
print(nome)
Quant_primeiro_nome = len(nome[0])

print(Quant)
print(f'Seu primeiro nome tem {Quant_primeiro_nome}')
