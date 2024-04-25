#Escreva um programa que leia o nome, e o sobrenome, CONCATENE em uma nova variável nome completo, e retorne para o usuário

nome = str(input('Qual o seu nome? '))
sobre_nome = str(input('E o seu sobrenome? '))

nome_completo = nome + ' ' + sobre_nome

print(f'O seu nome completo é: {nome_completo}! ')