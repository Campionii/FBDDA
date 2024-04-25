# Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.

dado = str(input('Escreva uma palavra: ')).strip().lower()

if dado[0] in ['a', 'e', 'i', 'o', 'u']:
    print(f'{dado} começa com uma vogal!')

else:
    print(f'{dado} começa com uma consoante!')