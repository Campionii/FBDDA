# Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10, entre 10 e 20 ou maior que  20.

n = int(input(f'Digite um número? '))

if n < 10 : print(f'{n} esta entre 0 a 10!')

elif n < 20 : print(f'{n} esta entre 10 e 20!')

else : print(f'{n} é maior que 20!')