# Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média, é insuficiente (menor que 6),
# suficiente (entre 6 e 7), bom (entre 7 e 9) ou excelente (9 ou maior).

n1 = float(input('Sua 1°nota: '))
n2 = float(input('Sua 2°nota: '))
n3 = float(input('Sua 3°nota: '))
n4 = float(input('Sua 4°nota: '))
n5 = float(input('Sua 5°nota: '))

media = (n1 + n2 + n3 + n4 + n5) /5

if media > 9:
    print('Excelente')

elif media > 7:
    print('Bom')

elif media < 6:
    print('suficiente')

else:
    print('Insuficiente')
