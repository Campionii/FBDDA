# Crie um programa onde serão informados diversos valores em uma lista.
# Caso o número já exista ele não será adicionado.
# No final, serão exibidos todos os valores únicos em ordem crescente

numeros = []

while True:

    n = int(input('Digite um numero: '))

    if n == 'sair':
        break

    if n in numeros:
        print('Já esta na lista')

    else:
        numeros.append(int(n))

print(sorted(numeros))
