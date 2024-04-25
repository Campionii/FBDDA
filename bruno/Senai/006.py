# Escreva um programa que leia 6 notas diferentes e faça a média do aluno

# primeira resolução

# Aluno = str(input('Qual o seu nome: '))
# n1 = int(input('Nota 1°: '))
# n2 = int(input('Nota 2°: '))
# n3 = int(input('Nota 3°: '))
# n4 = int(input('Nota 4°: '))
# n5 = int(input('Nota 5°: '))
# n6 = int(input('Nota 6°: '))
#
# s = n1 + n2 + n3 + n4 + n5 + n6
# m = s / 6
#
# print(f'A sua média: {m}')

# segunda tentativa aprendendo laço de repetição :)


soma_nota = 0

for i in range(6):
    nota = float(input(f'qual sua nota {i + 1}:'))
    soma_nota += nota

media = soma_nota / 6

print(f'A sua média: {media}!')
