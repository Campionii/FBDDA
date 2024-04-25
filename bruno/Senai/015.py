# Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

n = int(input('Qual número deseja saber se é ímpar ou par? '))

if n % 2 == 0:
    print(f'{n} é Par!')

else:
    print(f'{n} é Impar!')