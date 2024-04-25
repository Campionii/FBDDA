# Crie um programa que pede ao usuário para digitar dois números e, em seguida, divide o primeiro número pelo segundo número.
# No entanto, o programa deve ser capaz de lidar com a possibilidade de o usuário digitar um valor inválido,
# como uma string ou o número zero.
try:
    n1 = int(input('digite um numero: '))
    n2 = int(input('digite um outro numero: '))

    div = n1 / n2

except ZeroDivisionError:
    print('0 é numero invalido')

except ValueError:
    print('Valor invalido')

print(f''
          f'A divisao é {div}')









