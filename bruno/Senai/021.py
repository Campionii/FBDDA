# Escreva um programa que peça ao usuário um número de 1 a 7 e imprima o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).

n = int(input('Escolha um numero de 1 a 7: '))


if n == 1:
    print(f'{n} é segunda-feira')

elif n == 2:
    print(f'{n} é terça-feira')

elif n == 3:
    print(f'{n} é quarta-feira')

elif n == 4:
    print(f'{n} é quinta-feira')

elif n == 5:
    print(f'{n} é sexta-feira')

elif n == 6:
    print(f'{n} é sabado')

elif n == 7:
    print(f'{n} é domingo')

else:
    print(f'{n} não esta entre 1 e 7.')
