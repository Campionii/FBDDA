# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois, deve mostrar para cada palavra, suas vogais

palavras = ('barraco', 'cadeira', 'carro', 'macaco', 'louco', 'teclado')


for ele in palavras:
    print(ele + ' - ', end=' ')
    for letra in ele:
        if letra in 'AEIOUaeiou':
            print(letra, end=' ')
    print('\n')

