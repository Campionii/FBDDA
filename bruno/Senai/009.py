#Escreva um programa que leia um tipo de dado e usando a função type(), retorne ao usuário, qual o tipo de dado informado

dado = input('O que deseja analisar? ')
tipo_dado = type(dado).__name__
print(f'O {dado} é:', {tipo_dado})
