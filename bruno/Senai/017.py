# Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

dado = str(input('Escreva uma letra: '))

if dado == ['a', 'e', 'i', 'o', 'u']:
    print(f'{dado} é uma vogal!')

else:
    print(f'O {dado} é uma consoante!')