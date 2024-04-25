# Crie um programa que leia um nome, e mostre o primeiro e o último nome
# Saída esperada:
#
# Entrada: Luis Felipe Tatin Vlatkovic
# Primeiro nome: Luis
# Último nome: Vlatkovic

nome = input('O seu nome? ')
nome = nome.split()
primeiro_nome = nome[0]
ultimo_nome = nome[-1]
print(f'o primeiro nome é {primeiro_nome} e o ultimo {ultimo_nome}')


#resolucao 2

# Quant_nome = len(nome)
# print(nome[Quant_nome - 1])

